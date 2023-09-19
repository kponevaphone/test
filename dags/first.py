from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from datetime import datetime
from airflow import DAG

with DAG(
    dag_id="first",
    schedule=None,
    start_date=datetime.now(),
    catchup=False,
    tags=["first", "my", "dag"],
) as dag:
  airflow_with_kubernetes = KubernetesPodOperator(
    name="kubernetes_operator", 
    image="registry.localdev.me:5000/dag:latest",
    cmds=["python"],
    arguments=["main.py"],
    task_id="run-pod",
)

airflow_with_kubernetes.dry_run()
