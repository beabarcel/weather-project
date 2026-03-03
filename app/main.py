from db.connection import get_connection

def run():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT now();")
    result = cur.fetchone()

    print("Database successfully connected:", result)

    cur.close()
    conn.close()

if __name__ == "__main__":
    run()
