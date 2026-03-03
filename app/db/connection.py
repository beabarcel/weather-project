import psycopg2
from psycopg2.extras import RealDictCursor
from config.settings import DB_SETTINGS

def get_connection():
    return psycopg2.connect(
        host=DB_SETTINGS["host"],
        port=DB_SETTINGS["port"],
        dbname=DB_SETTINGS["database"],
        user=DB_SETTINGS["user"],
        password=DB_SETTINGS["password"],
        cursor_factory=RealDictCursor
    )
