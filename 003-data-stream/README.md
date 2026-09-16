# 003 — Data stream

Fragmenty kodu towarzyszące książce *Potoki danych. Leksykon kieszonkowy. Przenoszenie i przetwarzanie danych na potrzeby ich analizy* (James Densmore, Helion).

To samodzielne skrypty Python ilustrujące pojedyncze wzorce z książki — nie tworzą razem jednego pipeline'u i nie wymagają Airflow.

## Zawartość

- `extract_mysql_full.py`, `extract_mysql_incremental.py` — pełna vs. przyrostowa ekstrakcja z MySQL.
- `mysql_binlog.py`, `mysql_binlog_test.py` — change data capture z binloga MySQL.
- `extract_postgres_full.py` — ekstrakcja z Postgresa.
- `extract_mongodb.py`, `sample_mongodb.py` — odczyt z MongoDB.
- `extract_rest_api.py`, `open-notify.py`, `url_parse.py` — ekstrakcja z REST API.
- `copy_to_redshift.py`, `copy_truncate_redshift.py`, `redshift_test.py` — ładowanie do Amazon Redshift.
- `copy_into_snowflake.py` — ładowanie do Snowflake.
- `export_file_url.csv`, `order_extract.csv`, `order_extract_postgresql.csv` — przykładowe dane wejściowe/wyjściowe.
