# 001 — Wprowadzenie do Apache Airflow

Ćwiczenia z kursu Udemy o Apache Airflow — podstawowe koncepty na przykładach.

## Zawartość `dags/`

- `producer.py` / `consumer.py` — Datasets: jeden DAG produkuje dataset, drugi uruchamia się dopiero, gdy dataset zostanie zaktualizowany (`include/datasets.py`).
- `user_processing.py` — klasyczny ETL: `HttpSensor` czeka na dostępność API, `SimpleHttpOperator` pobiera dane, `PythonOperator` je przetwarza, `PostgresOperator`/`PostgresHook` zapisują do bazy.
- `group_dag.py` + `groups/groups_downloads.py`, `groups/groups_transforms.py` — grupowanie zadań przez `TaskGroup`.
- `parallel_dag.py` — równoległe wykonanie niezależnych zadań (`BashOperator`).
- `xcom_dag.py` / `xcom_dag_2.py` — przekazywanie danych między taskami przez XCom, drugi przykład dodatkowo pokazuje `TaskGroup`.
- `elastic_dag.py` + `plugins/hooks/elastic/elastic_hook.py` — własny Hook do Elasticsearch.
- `docker_dag.py` — uruchamianie zadania w kontenerze Docker przez `DockerOperator`.

## Jak uruchomić

```bash
cp env.example .env
docker compose up                       # standardowy setup
docker compose -f docker-compose-es.yaml up   # wariant z Elasticsearch (elastic_dag.py)
```

UI: `http://localhost:8080`, login/hasło: `airflow`/`airflow`.
