# Apache Airflow — notatki i projekty z nauki

Zbiór niezależnych od siebie projektów i ćwiczeń z Apache Airflow, zebranych podczas nauki orkiestracji danych: kursy Udemy, materiały Helion, oficjalne tutoriale Astronomer i Google Cloud.

To **nie jest** jeden spójny produkt — każdy katalog to osobne środowisko z własnym `docker-compose.yaml` lub projektem Astro CLI, uruchamiane niezależnie od pozostałych. Numeracja katalogów odzwierciedla kolejność, w jakiej powstawały, a nie zależności między nimi.

## Zawartość

| # | Katalog | Temat | Stack |
|---|---------|-------|-------|
| 001 | [introduction-to-apache-airflow](001-introduction-to-apache-airflow) | Podstawy: DAG-i, XCom, TaskGroups, sensory, integracja z Dockerem i Elasticsearch | Airflow (docker-compose) |
| 002 | [ingest-data-with-airflow-single-task](002-ingest-data-with-airflow-single-task) | Ingest danych jednym taskiem przez PyAirbyte (źródło S3) do cache'a BigQuery | Astro CLI, PyAirbyte, BigQuery |
| 003 | [data-stream](003-data-stream) | Fragmenty kodu z książki *Potoki danych. Leksykon kieszonkowy* (J. Densmore, Helion): ekstrakcja z Mongo/MySQL/Postgres/REST API, ładowanie do Redshift/Snowflake, CDC z binlogów MySQL | samodzielne skrypty Python (bez Airflow) |
| 004 | [airflow-core-load](004-airflow-core-load) | Data-aware scheduling: Datasets, dataset aliasy, warunkowe uruchamianie DAG-ów (w tym wariant pod Cloud Composer) | Airflow (docker-compose) |
| 005 | [dag-dependencies-trigger-dag-run-operator](005-dag-dependencies-trigger-dag-run-operator) | Zależności między DAG-ami przez `TriggerDagRunOperator` | Airflow (docker-compose) |
| 006 | [simple-extract-load-bq](006-simple-extract-load-bq) | Prosty pipeline extract-load do BigQuery z walidacją jakości danych i sensorem istnienia tabeli | Airflow (docker-compose), BigQuery |
| 007 | [apache-airflow-the-hands-on-guide](007-apache-airflow-the-hands-on-guide) | Projekt "Stock Market Pipeline": pobieranie danych giełdowych, MinIO jako data lake, Spark do transformacji, TaskFlow API | Astro CLI, MinIO, Spark |
| 008 | [astro-airflow-management-and-monitoring](008-astro-airflow-management-and-monitoring) | Zestaw mniejszych DAG-ów: sensory plikowe/HTTP/Python, branching, triggery, zmienne, Jinja, XCom | Astro CLI |
| 009 | [build-amazon-books-etl-job](009-build-amazon-books-etl-job) | ETL scrapujący listę książek z Amazon.pl (requests + BeautifulSoup) i zapisujący wynik do Postgresa | Airflow (docker-compose), Postgres |
| 010 | [codelabs-intro-cloud-composer.ipynb](010-codelabs-intro-cloud-composer.ipynb) | Notebook z oficjalnego Google Cloud Codelab: wprowadzenie do Cloud Composer (Airflow zarządzany przez GCP) | Jupyter, Google Cloud Composer |

## Jak uruchomić

Projekty dzielą się na dwa warianty lokalnego środowiska:

**Klasyczny `docker-compose` (001, 004, 005, 006, 009)**

```bash
cd 001-introduction-to-apache-airflow
cp env.example .env   # jeśli katalog go zawiera
docker compose up
```

UI Airflow dostępne pod `http://localhost:8080` (domyślnie login/hasło: `airflow`/`airflow`).

**Astro CLI (002, 007, 008)**

Wymaga zainstalowanego [Astro CLI](https://www.astronomer.io/docs/astro/cli/install-cli).

```bash
cd 002-ingest-data-with-airflow-single-task
astro dev start
```

**003** to zbiór samodzielnych skryptów (bez środowiska Airflow) — czytać jako materiał referencyjny, nie uruchamiać jako całość.

**010** to notebook Google Colab/Jupyter — działa w kontekście Google Cloud Codelab, nie lokalnie.

## Uwagi

- Część DAG-ów zawiera twarde wartości demo (np. dane logowania do lokalnego MinIO) — dotyczy wyłącznie usług uruchamianych lokalnie w Dockerze, nie prawdziwych zasobów.
- Repozytorium to materiał do nauki, nie referencyjna implementacja produkcyjna — różne katalogi celowo pokazują różne podejścia do podobnych problemów (np. klasyczne operatory vs TaskFlow API, `docker-compose` vs Astro CLI).
