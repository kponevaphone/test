from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from datetime import datetime
from airflow import DAG


with DAG(
    dag_id="162",
    start_date=datetime(2023, 9, 30),
    schedule='*/2 * * * *',
    catchup=False,
    max_active_runs=1,
    # schedule_interval='*/2 * * * *', 
    tags=["cam", "162"],
) as dag:
  first_task_main = KubernetesPodOperator(
    name="kubernetes_operator", 
    image="registry.localdev.me:5000/test:latest",
    cmds=["python"],
    arguments=["main.py"],
    task_id="run-pod-main",
)

first_task_main