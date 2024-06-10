from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from datetime import datetime
from airflow import DAG
from kubernetes.client import models as k8s


with DAG(
    dag_id="ids",
    start_date=datetime(2024, 4, 4),
    schedule='*/5 * * * *',
    catchup=False,
    max_active_runs=1,
    # schedule_interval='*/2 * * * *', 
    tags=["mi", "cn"],
) as dag:
  first_task = KubernetesPodOperator(
    # name="mi", 
    add_unique_suffix="mmii",
    image="devubu:5000/mi:latest",
    cmds=["python"],
    arguments=["mi5.py"],
    task_id="first_task",
)  
  second_task = KubernetesPodOperator(
    # name="cn",
    add_unique_suffix="ccnn",
    image="devubu:5000/cn:latest",
    cmds=["python"],
    arguments=["cn5.py"],
    startup_timeout_seconds=240,
    task_id="second_task",
)
first_task >> second_task