import os
from dotenv import load_dotenv

load_dotenv()

DB_SETTINGS = {
    "host": os.getenv("DB_HOST", "postgres"),
    "port": int(os.getenv("DB_PORT", 5432)),
    "database": os.getenv("POSTGRES_DB", "weather_db"),
    "user": os.getenv("POSTGRES_USER", "weather_user"),
    "password": os.getenv("POSTGRES_PASSWORD", "weather_pass"),
}

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
