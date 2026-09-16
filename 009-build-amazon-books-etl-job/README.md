# 009 — Amazon Books ETL

Prosty pipeline scrapujący wyniki wyszukiwania książek na Amazon.pl i zapisujący je do Postgresa.

## Przepływ (`dags/fetch_and_store_amazon_books.py`)

1. `fetch_book_data` — pobiera listę książek (tytuł, autor, cena, ocena) ze stron wyników wyszukiwania Amazon.pl przez `requests` + `BeautifulSoup`, wynik trafia do XCom.
2. `create_table` — tworzy (jeśli nie istnieje) tabelę `book_data` w Postgresie.
3. `insert_book_data` — zapisuje pobrane rekordy do tabeli.

## Jak uruchomić

```bash
docker compose up
```

UI: `http://localhost:8080`. Wymaga skonfigurowanego w Airflow connection do Postgresa o id `books_connection` (Admin → Connections).

## Uwaga

Scraping serwisu Amazon łamie jego regulamin i może przestać działać w dowolnym momencie (zmiana HTML, blokada IP/user-agenta) — to ćwiczenie edukacyjne, nie rozwiązanie do użytku produkcyjnego.
