from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

def print_world() -> None:
    print("world")

# with 구문으로 DAG 정의를 시작합니다.
with DAG(
    dag_id="hello_world",  # DAG의 식별자용 아이디입니다.
    description="My First DAG",  # DAG에 대해 설명합니다.
    start_date=days_ago(2),  # DAG 정의 기준 2일 전부터 시작합니다.
    schedule_interval=timedelta(days=1),  # 1일을 주기로 실행합니다.
    tags=["examples"],
    default_args={  # 모든 오퍼레이터에 들어갈 공통 파라미터를 정의합니다.
        "owner": "cjlotto",  # 이 작업의 오너입니다. 보통 작업을 담당하는 사람 이름을 넣습니다.
        "retries": 3,  # 이 Task가 실패한 경우, 3번 재시도 합니다.
        "retry_delay": timedelta(minutes=5),  # 재시도하는 시간 간격은 5분입니다.
    }
) as dag:

    t1 = BashOperator(
        task_id="print_hello",
        bash_command="echo Hello",
    )

    t2 = PythonOperator(
        task_id="print_world",
        python_callable=print_world,
    )

    t1 >> t2
