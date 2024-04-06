from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from datetime import datetime
from airflow import DAG
from kubernetes.client import models as k8s


with DAG(
    dag_id="gpu_test",
    start_date=datetime(2024, 4, 4),
    schedule='*/5 * * * *',
    catchup=False,
    max_active_runs=1,
    # schedule_interval='*/2 * * * *', 
    tags=["cam", "gpu_test"],
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
    # cluster_context='nvidia',
    image="devubu:5000/cn:latest",
    cmds=["python"],
    arguments=["test.py"],
    env_vars={"NVIDIA_VISIBLE_DEVICES": "all", "NVIDIA_DRIVER_CAPABILITIES":"all", "CUDA_VISIBLE_DEVICES":"0" },
    # container_resources=k8s.V1ResourceRequirements(limits={"nvidia.com/gpu": "1"},),
    container_resources=k8s.V1ResourceRequirements(
        requests={
            'cpu': '800m',
            'memory': '5000M',
            'ephemeral-storage': '3000M',
        },
        limits={
            'cpu': '1000m',
            'memory': '6000M',
            'ephemeral-storage': '3000M',
            'nvidia.com/gpu': 1, # or 'amd.com/gpu'
        },
    ),

    # tolerations = [k8s.V1Toleration(key="nvidia.com/gpu", value="true", operator="Equal", effect="NoSchedule")],
    task_id="pod-second_task",
)
# sudo docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
first_task >> second_task