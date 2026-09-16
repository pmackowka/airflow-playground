# 007 — Stock Market Pipeline

Projekt z kursu o Apache Airflow: pipeline pobierający dane giełdowe, przechowujący je w MinIO (lokalny data lake kompatybilny z S3) i przetwarzający przez Sparka.

## Zawartość

- `dags/stock_market.py` — główny DAG: sprawdza dostępność API giełdowego, pobiera dane, zapisuje je do MinIO, uruchamia zadanie Sparka do transformacji.
- `dags/taskflow_classic.py`, `dags/taskflow_decorators.py`, `dags/taskflow_decorators_mix.py` — porównanie klasycznego stylu definiowania DAG-ów z TaskFlow API (dekoratory `@task`/`@dag`).
- `include/helpers/minio.py` — helper do komunikacji z MinIO.
- `include/stock_market/tasks.py` — logika poszczególnych kroków pipeline'u.
- `spark/` — obrazy Dockera dla mastera i workera Sparka oraz notebook transformujący dane (`spark/notebooks/stock_transform`).

MinIO w `spark/notebooks/stock_transform/Dockerfile` używa danych logowania demo (`minio`/`minio123`) — to lokalny kontener bez wystawionych na zewnątrz danych, nie prawdziwe poświadczenia.

## Jak uruchomić

Wymaga [Astro CLI](https://www.astronomer.io/docs/astro/cli/install-cli).

```bash
astro dev start
```

Uruchomi to Airflow (webserver, scheduler, triggerer, Postgres) oraz dodatkowe kontenery zdefiniowane w `docker-compose.override.yml`: MinIO, Spark (master/worker) i Metabase do wizualizacji wyników.

UI Airflow: `http://localhost:8080` (login/hasło: `admin`/`admin`).
