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
    name="kuboper", 
    image="devubu:5000/pr:latest",
    cmds=["python"],
    arguments=["pr9.py"],
    task_id="pod-first_task",
)  
  second_task = KubernetesPodOperator(
    name="kuboper", 
    # cluster_context='nvidia',
    image="devubu:5000/cn:latest",
    cmds=["python"],
    arguments=["cn9.py"],
    env_vars={"NVIDIA_VISIBLE_DEVICES": "all", "NVIDIA_DRIVER_CAPABILITIES":"all" }, #"CUDA_VISIBLE_DEVICES":"0"
    container_resources=k8s.V1ResourceRequirements(requests={'nvidia.com/gpu': 1,}, limits={'nvidia.com/gpu': 1,}),
    # container_resources=k8s.V1ResourceRequirements(limits={"nvidia.com/gpu": 1},),
    tolerations = [k8s.V1Toleration(key="nvidia.com/gpu", operator="Exists", effect="NoExecute", seconds='300')],
    # Exists
    # tolerations=[{'key': NODE_POOL, 'operator': 'Equal', 'value': 'true', 'effect': "NoSchedule"},
    #               {'key': "nvidia.com/gpu", 'operator': 'Equal','value': 'present', 'effect': "NoSchedule" }],
    task_id="pod-second_task",
)
# sudo docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
first_task >> second_task