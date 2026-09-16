# 008 — Zarządzanie i monitorowanie Airflow

Zestaw niezależnych, mniejszych DAG-ów (materiały Helion) ilustrujących pojedyncze mechanizmy Airflow.

## Zawartość `dags/`

- `bash-operator.py`, `python-operator.py`, `python-operator-scheduler.py`, `http-operator.py` — podstawowe operatory.
- `branch.py`, `triggers1.py`, `triggers2.py` — branching (`BranchPythonOperator`) i reguły wyzwalania (`trigger_rule`).
- `file-sensor.py`, `python-sensor.py`, `http-sensor.py` — sensory: na plik, na warunek w Pythonie, na endpoint HTTP.
- `variable.py`, `params.py`, `jinja.py` — Airflow Variables, parametry DAG-a, szablony Jinja.
- `xcom.py`, `order_task.py`, `default_dag_args.py`, `example.py`, `example-2.py`, `exampledag.py` — pozostałe przykłady: XCom, kolejność zadań, domyślne argumenty.

## Jak uruchomić

Wymaga [Astro CLI](https://www.astronomer.io/docs/astro/cli/install-cli).

```bash
astro dev start
```

UI Airflow: `http://localhost:8080` (login/hasło: `admin`/`admin`).
