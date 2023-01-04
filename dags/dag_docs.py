from datetime import datetime, timedelta
from time import sleep

from airflow import DAG
from airflow.operators.python import PythonOperator
from pendulum.tz.timezone import Timezone

with DAG(
    dag_id="03_documentation",
    description="문서화를 추가하는 DAG 예제입니다.",
    default_args={
        "owner": "heumsi",
        "retries": 1,
        "retry_delay": timedelta(minutes=1),
    },
    start_date=datetime(2022, 1, 20, tzinfo=Timezone("Asia/Seoul")),
    schedule_interval="@once",
    tags=["examples", "03_visualization_and_documentation_dags"],
    doc_md="""
        ## 문서화 추가

        코드에서 DAG 인스턴스 생성 시 doc_md에 만저열을 넘겨주면 된다.
        마크다운으로 쓰는 것이 가능하다.
    """,
) as dag:

    def dump() -> None:
        sleep(3)

    task_1 = PythonOperator(
        task_id="task_1", python_callable=dump, doc_md="task에 대해서도 문서화를 추가 할 수 있다."
    )
    task_2 = PythonOperator(task_id="task_2", python_callable=dump)
    task_3 = PythonOperator(task_id="task_3", python_callable=dump)

    task_1 >> task_2 >> task_3
