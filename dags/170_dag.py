from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from datetime import datetime
from airflow import DAG


with DAG(
    dag_id="170",
    start_date=datetime(2024, 4, 5),
    schedule='*/5 * * * *',
    catchup=False,
    max_active_runs=1,
    schedule_interval='*/5 * * * *', 
    tags=["cam", "170"],
) as dag:
  first_task_main = KubernetesPodOperator(
    name="kubernetes_operator", 
    image="devubu:5000/pr:latest",
    cmds=["python"],
    arguments=["pr9.py"],
    task_id="run-pod-main",
)

first_task_main