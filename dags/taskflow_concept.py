from datetime import datetime

from airflow.decorators import dag, task
from pendulum.tz.timezone import Timezone


@dag(
    dag_id="01_concept",
    description="Taskflow API",
    default_args={
        "owner": "luke",
        "retries": 0,
    },
    start_date=datetime(2022, 1, 20, tzinfo=Timezone("Asia/Seoul")),
    schedule_interval="@once",
    tags=["examples", "06_taskflow_api"],
)
def main():
    """Taskflow API
    1. print_hello(), get_first_word_from_param_and_return() 실행
    2. get_first_word_from_param_and_return() 성공 하면, get_last_word_from_param()을 실행
    """

    @task
    def print_hello() -> None:
        """hello 출력"""

        print("hello")

    @task
    def get_first_word_from_param_and_return(param: str) -> str:
        """문자열 param의 첫 번째 단어 출력 후 param 반환"""

        first_word = param.split()[0]
        print(first_word)
        return param

    @task
    def get_last_word_from_param(param: str) -> None:
        """문자열 param의 마지막 단어 출력"""

        last_word = param.split()[-1]
        print(last_word)

    @task
    def print_kwargs(**kwargs) -> None:
        print(kwargs)

    print_hello()
    ret = get_first_word_from_param_and_return("welcome to airflow")
    get_last_word_from_param(ret)
    print_kwargs()


dag = main()
