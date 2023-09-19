from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from datetime import datetime
from airflow import DAG

with DAG(
    dag_id="airflow",
    schedule=None,
    start_date=datetime.now(),
    catchup=False,
    tags=["test"],
) as dag:
  airflow_with_kubernetes = KubernetesPodOperator(
    name="kubernetes_operator", 
    image="alekseyolg/airflow-with-kubernetes:v1.0",
    cmds=["python"],
    arguments=["first-script.py"],
    task_id="run-pod-with-kubernetes",
)

airflow_with_kubernetes.dry_run()
