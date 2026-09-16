# 004 — Data-aware scheduling (Datasets)

Przykłady mechanizmu Datasets w Apache Airflow: uruchamianie DAG-ów na podstawie zaktualizowania danych, a nie tylko harmonogramu czasowego.

## Zawartość `dags/`

- `conditional_dataset.py` / `conditional_dataset_basic.py` — warunkowe uruchamianie DAG-a na podstawie kombinacji wielu datasetów.
- `conditional_dataset_composer_gcp.py` — ten sam wzorzec dostosowany pod Google Cloud Composer.
- `dataset_alias_example_alias_consumer.py` / `dataset_alias_example_alias_consumer_with_no_taskflow.py` — dataset aliasy, w wersji z TaskFlow API i bez.
- `example_bash_operator.py`, `example_branch_datetime_operator.py` — przykładowe DAG-i z oficjalnej dokumentacji Airflow (branching po dacie/godzinie).

## Jak uruchomić

```bash
docker compose up
```

UI: `http://localhost:8080`.
