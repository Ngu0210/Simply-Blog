import os
import psycopg2

connection = psycopg2.connect(
        database="simply_blog",
        user="postgres",
        password=os.getenv("DBPASS"),
        host="23.22.149.187",
        port="5432"
    )

cursor = connection.cursor()

