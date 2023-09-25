from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from datetime import datetime
from airflow import DAG

with DAG(
    dag_id="first_dag",
    schedule=None,
    start_date=datetime.now(),
    catchup=False,
    tags=["first", "dag"],
) as dag:
  first_task = KubernetesPodOperator(
    name="kubernetes_operator", 
    image="registry.localdev.me:5000/test:latest",
    cmds=["python"],
    arguments=["main1.py"],
    task_id="run-pod-first_task",
)
  second_task = KubernetesPodOperator(
    name="kubernetes_operator", 
    image="registry.localdev.me:5000/test:latest",
    cmds=["python"],
    arguments=["main2.py"],
    task_id="run-pod-second_task",
)
  three_task = KubernetesPodOperator(
    name="kubernetes_operator", 
    image="registry.localdev.me:5000/test:latest",
    cmds=["python"],
    arguments=["main3.py"],
    task_id="run-pod-three_task",
)

  first_task >> second_task >> three_task