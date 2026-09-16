from airflow.decorators import dag, task
from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow.sensors.filesystem import FileSensor

HELION_DIR = "/usr/local/airflow/include"
HELION_FILE = f"{HELION_DIR}/helion_airflow.txt"

# Funkcja placeholder dla EmptyOperator
@task
def start_task():
    return 'Start task'

# Definicja DAG-a z użyciem dekoratora @dag
@dag(
    dag_id='file_sensor',
    schedule_interval=None,
    start_date=datetime(2023, 9, 14),
    tags=['Helion'],
    catchup=False
)
def file_sensor_dag():
    # Definiowanie zadań
    start = start_task()  # Zadanie startowe jako placeholder

    create_file = BashOperator(
        task_id='create_file',
        bash_command=(
            f"mkdir -p {HELION_DIR} && "
            f"echo 'Airflow' > {HELION_FILE}"
        )
    )

    check_file = FileSensor(
        task_id='check_file',
        filepath=HELION_FILE,
        poke_interval=5,  # Co 5 sekund sprawdza, czy plik istnieje
        timeout=60  # Maksymalny czas oczekiwania 60 sekund
    )

    cat_file = BashOperator(
        task_id='cat_file',
        bash_command=f"cat {HELION_FILE}"
    )

    # Definiowanie kolejności zadań
    start >> create_file >> check_file >> cat_file

# Inicjalizacja DAG-a
dag = file_sensor_dag()
