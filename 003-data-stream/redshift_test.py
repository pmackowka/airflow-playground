import configparser
import psycopg2

# Dane konfiguracyjne do Redshift - patrz pipeline.conf (poza repo, sekcja [aws_creds])
parser = configparser.ConfigParser()
parser.read("pipeline.conf")
host = parser.get("aws_creds", "host")
port = parser.get("aws_creds", "port")
user = parser.get("aws_creds", "username")
password = parser.get("aws_creds", "password")
dbname = parser.get("aws_creds", "database")

try:
    rs_conn = psycopg2.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        dbname=dbname
    )
    print("Połączenie udane!")
except psycopg2.OperationalError as e:
    print(f"Błąd połączenia: {e}")
