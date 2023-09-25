from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from datetime import datetime
from airflow import DAG

with DAG(
    dag_id="influx_dag",
    schedule=None,
    start_date=datetime.now(),
    catchup=False,
    tags=["influx", "dag"],
) as dag:
  first_task_influx = KubernetesPodOperator(
    name="kubernetes_operator", 
    image="registry.localdev.me:5000/test:latest",
    cmds=["python"],
    arguments=["inf.py"],
    task_id="run-pod-influx",
)

first_task_influx