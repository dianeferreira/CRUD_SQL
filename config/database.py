import psycopg2

connecting = psycopg2.connect(
    dbname="teste", user="postgres", password="postgres", host="localhost")

cursor = connecting.cursor()

