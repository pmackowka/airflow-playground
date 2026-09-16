# 002 — Ingest danych jednym taskiem (PyAirbyte + BigQuery)

Szablon projektu Astronomer (`astro dev init`) rozszerzony o realny pipeline ingestu danych.

## Zawartość

- `dags/ingest_data_with_airflow_single_task.py` — jeden task ekstrahuje dane z S3 przez [PyAirbyte](https://airbyte.com/product/pyairbyte) (uruchamiane w osobnym venv skonfigurowanym w `Dockerfile`) i ładuje je do cache'a BigQuery, drugi task sprawdza liczbę wczytanych wierszy.
- `dags/exampledag.py` — domyślny przykład wygenerowany przez `astro dev init`.
- `retail_transaction_dataset.csv` — przykładowe dane wejściowe.
- `tests/dags/test_dag_example.py` — test integralności DAG-ów (uruchamiany też w CI Astronomera).

## Wymagania przed uruchomieniem

DAG oczekuje realnych danych dostępowych, których nie ma w repo:
- kluczy AWS (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`) w lokalnym `.env`,
- własnego `project_name` GCP i pliku klucza service account (`credentials_path`) w kodzie zamiast wartości placeholder.

## Jak uruchomić

Wymaga [Astro CLI](https://www.astronomer.io/docs/astro/cli/install-cli).

```bash
astro dev start
```

Uruchomi to 4 kontenery: Postgres (metadata DB), webserver, scheduler, triggerer.

UI Airflow: `http://localhost:8080` (login/hasło: `admin`/`admin`). Postgres: `localhost:5432/postgres`.
