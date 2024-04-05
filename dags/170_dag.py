from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from datetime import datetime
from airflow import DAG


with DAG(
    dag_id="170",
    start_date=datetime(2023, 9, 30),
    schedule='*/2 * * * *',
    catchup=False,
    max_active_runs=1,
    # schedule_interval='*/2 * * * *', 
    tags=["cam", "170"],
) as dag:
  first_task_main = KubernetesPodOperator(
    name="kubernetes_operator", 
    image="devubu:5000/pr:latest",
    cmds=["python"],
    arguments=["pr7.py"],
    task_id="run-pod-main",
)

first_task_main