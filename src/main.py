import os
import psycopg2

for key, value in os.environ.items():
    print(f"{key}: {value}")


conn = psycopg2.connect(
    dbname=os.getenv("PSQL_DATABASE"),
    user=os.getenv("PSQL_USERNAME"),
    password=os.getenv("PSQL_PASSWORD"),
    host=os.getenv("PSQL_HOST"),
    port=os.getenv("PSQL_PORT"),
)

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS sample_table (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100)
    )
""")

cur.execute("INSERT INTO sample_table (name) VALUES ('Row1')")
cur.execute("INSERT INTO sample_table (name) VALUES ('Row2')")
cur.execute("INSERT INTO sample_table (name) VALUES ('Row3')")

conn.commit()

cur.execute("SELECT * FROM sample_table")
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()
