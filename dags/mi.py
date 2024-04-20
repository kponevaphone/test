from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from datetime import datetime
from airflow import DAG
from kubernetes.client import models as k8s


with DAG(
    dag_id="mi",
    start_date=datetime(2024, 4, 4),
    schedule='*/5 * * * *',
    catchup=False,
    max_active_runs=1,
    # schedule_interval='*/2 * * * *', 
    tags=["cam", "mi"],
) as dag:
  first_task = KubernetesPodOperator(
    name="mi", 
    image="devubu:5000/mi:latest",
    cmds=["python"],
    arguments=["mi3.py"],
    task_id="pod-first_task",
)  
  second_task = KubernetesPodOperator(
    name="yol", 
    image="devubu:5000/cn:latest",
    cmds=["python"],
    arguments=["mi2.py"],
    task_id="pod-second_task",
)
first_task >> second_task