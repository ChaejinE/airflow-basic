from datetime import datetime

from airflow import DAG
from airflow.models import Variable
from airflow.operators.python import PythonOperator
from pendulum.tz.timezone import Timezone

with DAG(
    dag_id="02_variables",
    description="Variables를 활용하는 DAG 예제입니다.",
    default_args={
        "owner": "heumsi",
        "retries": 0,
    },
    start_date=datetime(2022, 1, 20, tzinfo=Timezone("Asia/Seoul")),
    schedule_interval="@once",
    tags=["examples", "05_etc_features"],
) as dag:

    def print_variabels() -> None:
        hello = Variable.get(key="hello")
        print(hello)

        not_existing_key = Variable.get(
            key="not_existing_key", default_var="default value"
        )
        print(not_existing_key)

        json_data = Variable.get(key="json_data", deserialize_json=True)
        print(json_data["welcome"])
        print(json_data["author"])

    def print_variables_through_template(
        hello: str,
        author: str,
        not_existing_key: str,
    ) -> None:
        print(hello)
        print(author)
        print(not_existing_key)

    task_1 = PythonOperator(task_id="print_variables", python_callable=print_variabels)
    task_2 = PythonOperator(
        task_id="print_variabels_through_templates",
        python_callable=print_variables_through_template,
        op_kwargs={
            "hello": "{{ var.value.hello }}",
            "author": "{{ var.json.json_data.author }}",
            "not_existing_key": "{{ var.value.get('not_existing_key', 'default value') }}",
        },
    )

    task_1 >> task_2
