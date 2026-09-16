from airflow import DAG
from datetime import datetime
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from airflow.sensors.python import PythonSensor

HELION_FILE = "/usr/local/airflow/include/helion_airflow.txt"


def is_enough_len(minimum: int):
    with open(HELION_FILE, "r") as file:
        data = file.read()

    if len(data) > minimum:
        return True
    else:
        return False


with DAG(
    dag_id='python-sensor',
    schedule_interval=None,
    start_date=datetime(2023, 9, 14),
    tags=['Helion'],
    catchup=False
):

    start = EmptyOperator(
        task_id='start'
    )

    python_check = PythonSensor(
        task_id='python_check',
        python_callable=is_enough_len,
        op_args=[10],
        mode='poke',
        timeout=15,
        poke_interval=5
    )

    echo_bash = BashOperator(
        task_id='echo_bash',
        bash_command="echo 'KONIEC'"
    )

    start >> python_check >> echo_bash
