from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from datetime import datetime
from airflow import DAG

with DAG(
    dag_id="189_dag",
    schedule=None,
    start_date=datetime.now(),
    catchup=False,
    tags=["189", "dag"],
) as dag:
  first_task_influx = KubernetesPodOperator(
    name="kubernetes_operator", 
    image="registry.localdev.me:5000/test:latest",
    cmds=["python"],
    arguments=["189.py"],
    task_id="run-pod-189",
)
  second_task = KubernetesPodOperator(
    name="kubernetes_operator", 
    image="registry.localdev.me:5000/test:latest",
    cmds=["python"],
    arguments=["189.py"],
    task_id="run-pod-189",
)

first_task_influx