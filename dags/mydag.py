from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from datetime import datetime
from airflow import DAG

with DAG(
    dag_id="mydag",
    schedule=None,
    start_date=datetime.now(),
    catchup=False,
    tags=["my", "dag"],
) as dag:
  first_task = KubernetesPodOperator(
    name="kubernetes_operator", 
    image="registry.localdev.me:5000/test:latest",
    cmds=["python"],
    arguments=["main.py"],
    task_id="run-pod1",
)
  second_task = KubernetesPodOperator(
    name="kubernetes_operator", 
    image="registry.localdev.me:5000/test:latest",
    cmds=["python"],
    arguments=["main.py"],
    task_id="run-pod2",
)
  three_task = KubernetesPodOperator(
    name="kubernetes_operator", 
    image="registry.localdev.me:5000/test:latest",
    cmds=["python"],
    arguments=["main.py"],
    task_id="run-pod3",
)

  first_task >> second_task >> three_task