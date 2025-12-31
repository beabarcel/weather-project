import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", 5432),
    "dbname": os.getenv("DB_NAME", "weather_db"),
    "user": os.getenv("DB_USER", "weather_user"),
    "password": os.getenv("DB_PASSWORD", "weather_pass"),
}

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
