from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from datetime import datetime
from airflow import DAG


with DAG(
    dag_id="170",
    start_date=datetime(2024, 4, 4),
    schedule='*/5 * * * *',
    catchup=False,
    max_active_runs=1,
    # schedule_interval='*/2 * * * *', 
    tags=["cam", "170"],
) as dag:
  first_task = KubernetesPodOperator(
    name="kubernetes_operator", 
    image="devubu:5000/pr:latest",
    cmds=["python"],
    arguments=["pr9.py"],
    task_id="pod-first_task",
)
  second_task = KubernetesPodOperator(
    name="kubernetes_operator", 
    image="devubu:5000/cn:latest",
    cmds=["python"],
    arguments=["cn9.py"],
    env_vars={"NVIDIA_VISIBLE_DEVICES": "all", "NVIDIA_DRIVER_CAPABILITIES":"all"},
    resources={'limit_memory': "250M", 'limit_cpu': "100m", 'nvidia.com/gpu':"1"},
    task_id="pod-second_task",
)

first_task >> second_task