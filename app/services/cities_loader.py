from db.connection import get_connection

def load_cities(file_path: str, limit: int = None):
    conn = get_connection()
    cur = conn.cursor()

    batch = []
    inserted = 0
    batch_size = 15000

    with open(file_path, encoding="utf-8") as file:
        for line in file:
            columns = line.strip().split("\t")

            name = columns[1]
            latitude = float(columns[4])
            longitude = float(columns[5])
            country = columns[8]

            batch.append((name, country, latitude, longitude))
            inserted += 1

            if len(batch) >= batch_size:
                cur.executemany("""
                                INSERT INTO cities (name, country, latitude, longitude)
                                VALUES (%s, %s, %s, %s)
                                ON CONFLICT (name, country) DO NOTHING
                            """, batch)
                conn.commit()
                batch.clear()

            if limit and inserted >= limit:
                break

    if batch:
        cur.executemany("""
                        INSERT INTO cities (name, country, latitude, longitude)
                        VALUES (%s, %s, %s, %s)
                        ON CONFLICT (name, country) DO NOTHING
                    """, batch)
        conn.commit()

    cur.close()
    conn.close()

    print(f"{inserted} cities processed.")