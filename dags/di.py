from airflow.decorators import dag, task
from datetime import datetime

import os
import json
import requests
from kubernetes.client import models as k8s

new_config ={ "pod_override": k8s.V1Pod(
                metadata=k8s.V1ObjectMeta(labels={"purpose": "pod-override-example"}),
                spec=k8s.V1PodSpec(
                    containers=[
                        k8s.V1Container(
                            name="base",
                            env=[
                                k8s.V1EnvVar(name="STATE", value="wa")
                                ],
                            )
                        ]
                    )
                )
            }

default_args = {
    'start_date': datetime(2021, 1, 1)
}

@dag('k8s_executor_example', schedule_interval='@daily', default_args=default_args, catchup=False)
def taskflow():

    @task(executor_config=new_config)
    def get_testing_increase():
        """
        Gets totalTestResultsIncrease field from Covid API for given state and returns value
        """
        url = 'https://covidtracking.com/api/v1/states/'
        res = requests.get(url+'{0}/current.json'.format(os.environ['STATE']))
        return{'testing_increase': json.loads(res.text)['totalTestResultsIncrease']}

    get_testing_increase()

dag = taskflow()