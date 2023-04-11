from datetime import datetime, timedelta
from airflow.decorators import dag
from airflow.operators.bash import BashOperator


default_args = {
    "owner": "Shuvo"
}


@dag(dag_id='dag_v2', default_args=default_args, start_date=datetime(2021, 1, 1), schedule="@daily")
def generate_dag():
    task_1 = BashOperator(task_id="task_1", bash_command="echo This is Task 1")
    task_2 = BashOperator(task_id="task_2", bash_command="echo This is Task 2")
    task_1.set_upstream(task_2)


generate_dag()
