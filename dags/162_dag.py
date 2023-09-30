from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from datetime import datetime
from airflow import DAG


default_args = {
  'schedule_interval': '*/1 * * * *' #..every 10 minutes
}

with DAG(
    dag_id="162",
    schedule=None,
    start_date=datetime.now(),
    catchup=False,
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