import psycopg2
import os

conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
)

cur = conn.cursor()

cur.execute(
    """
    INSERT INTO cities (name, country, latitude, longitude)
    VALUES (%s, %s, %s, %s)
    ON CONFLICT (name, country) DO NOTHING
    """,
    ("Test City", "TC", 0.0, 0.0)
)

conn.commit()

print("City inserted successfully!")

cur.close()
conn.close()
