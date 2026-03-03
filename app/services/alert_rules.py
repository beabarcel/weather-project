ALERT_RULES = [
    {
        "type": "HIGH_TEMPERATURE",
        "field": "temperature",
        "threshold": 35,
        "operator": ">="
    },
    {
        "type": "LOW_TEMPERATURE",
        "field": "temperature",
        "threshold": 5,
        "operator": "<="
    },
    {
        "type": "HIGH_HUMIDITY",
        "field": "humidity",
        "threshold": 90,
        "operator": ">="
    },
    {
        "type": "LOW_HUMIDITY",
        "field": "humidity",
        "threshold": 30,
        "operator": "<="
    }
]


def check_alerts(data):
    alerts = []

    for rule in ALERT_RULES:
        value = data.get(rule["field"])
        if value is None:
            continue

        if rule["operator"] == ">=" and value >= rule["threshold"]:
            alerts.append({
                "type": rule["type"],
                "threshold": rule["threshold"],
                "actual_value": value
            })

        if rule["operator"] == "<=" and value <= rule["threshold"]:
            alerts.append({
                "type": rule["type"],
                "threshold": rule["threshold"],
                "actual_value": value
            })

    return alerts
