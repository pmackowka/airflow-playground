# 005 — Zależności między DAG-ami (`TriggerDagRunOperator`)

Przykład wyzwalania jednego DAG-a przez drugi za pomocą `TriggerDagRunOperator`, jako alternatywa dla Datasets przy budowaniu zależności cross-DAG.

## Zawartość `dags/`

- `trigger_dag.py` — DAG nadrzędny, wyzwala `target_dag` po zakończeniu własnych zadań.
- `target_dag.py` — DAG docelowy, uruchamiany przez `trigger_dag`.

## Jak uruchomić

```bash
docker compose up
```

UI: `http://localhost:8080`.
