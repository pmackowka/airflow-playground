# 006 — Extract-load do BigQuery z kontrolą jakości danych

Pipeline oparty o wzorzec z oficjalnych materiałów Astronomer: ładowanie danych o pożarach lasów (zbiór "forestfire") do BigQuery wraz z automatyczną walidacją jakości wczytanych danych.

## Zawartość

- `dags/006-simple-extract-load-bq.py` — tworzy dataset i tabelę w BigQuery (jeśli nie istnieją), ładuje dane, uruchamia kontrole jakości wierszy (`BigQueryCheckOperator`, `BigQueryValueCheckOperator`).
- `dags/include/sql/load_bigquery_forestfire_data.sql` — zapytanie ładujące dane.
- `dags/include/sql/row_quality_bigquery_forestfire_check.sql` — zapytanie kontroli jakości danych.
- `dags/include/validation/forestfire_validation.json` — reguły walidacji.

## Wymagania

DAG oczekuje skonfigurowanych w UI Airflow (Admin → Connections/Variables):
- Connection `bigquery` (typ Google Cloud),
- Variable `gcp_project_id`.

## Jak uruchomić

```bash
cp env.example .env
docker compose up
```

UI: `http://localhost:8080`, login/hasło: `airflow`/`airflow`.
