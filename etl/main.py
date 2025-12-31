from datetime import datetime, timezone

from config import OPENWEATHER_API_KEY
from db import get_connection
from weather_api import get_weather
from rules import check_alerts


def run_etl():
    if not OPENWEATHER_API_KEY:
        raise RuntimeError("OPENWEATHER_API_KEY is not configured")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT id, latitude, longitude FROM cities")
    cities = cursor.fetchall()

    if not cities:
        print("No cities found in database.")
        return

    for city in cities:
        city_id = city["id"]
        latitude = city["latitude"]
        longitude = city["longitude"]

        weather_response = get_weather(latitude, longitude, OPENWEATHER_API_KEY)

        weather_data = {
            "temperature": weather_response["main"]["temp"],
            "feels_like": weather_response["main"]["feels_like"],
            "humidity": weather_response["main"]["humidity"],
            "condition": weather_response["weather"][0]["main"],
        }

        collected_at = datetime.now(timezone.utc)

        cursor.execute(
            """
            INSERT INTO weather_readings
            (city_id, temperature, feels_like, humidity, condition, collected_at)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (
                city_id,
                weather_data["temperature"],
                weather_data["feels_like"],
                weather_data["humidity"],
                weather_data["condition"],
                collected_at,
            ),
        )

        alerts = check_alerts(weather_data)
        for alert in alerts:
            cursor.execute(
                """
                INSERT INTO alerts
                (city_id, alert_type, threshold, actual_value)
                VALUES (%s, %s, %s, %s)
                """,
                (
                    city_id,
                    alert["type"],
                    alert["threshold"],
                    alert["actual_value"],
                ),
            )

    connection.commit()
    cursor.close()
    connection.close()

    print("ETL process completed successfully.")


if __name__ == "__main__":
    run_etl()
