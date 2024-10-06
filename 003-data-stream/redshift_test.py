import psycopg2

try:
    rs_conn = psycopg2.connect(
        host="***REMOVED-REDSHIFT-HOST***",
        port="5439",
        user="awsuser",
        password="***REMOVED***",
        dbname="dev"
    )
    print("Połączenie udane!")
except psycopg2.OperationalError as e:
    print(f"Błąd połączenia: {e}")