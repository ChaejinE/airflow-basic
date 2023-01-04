from datetime import datetime, timedelta
from time import sleep

from airflow import DAG
from airflow.operators.python import PythonOperator
from pendulum.tz.timezone import Timezone

with DAG(
    dag_id="parallel_tasks",
    description="parallel_task",
    default_args={
        "owner": "luke",
        "retries": 1,
        "retry_delay": timedelta(minutes=1),
    },
    start_date=datetime(2023, 1, 20, tzinfo=Timezone("Asia/Seoul")),
    schedule_interval="@once",
    tags=["examples", "various_task_flows"],
) as dag:

    def dump() -> None:
        sleep(3)

    task_1 = PythonOperator(task_id="task_1", python_callable=dump)
    task_2 = PythonOperator(task_id="task_2", python_callable=dump)
    task_3 = PythonOperator(task_id="task_3", python_callable=dump)
    task_4 = PythonOperator(task_id="task_4", python_callable=dump)
    task_5 = PythonOperator(task_id="task_5", python_callable=dump)

    task_1 >> task_2 >> task_5
    task_3 >> task_4 >> task_5
