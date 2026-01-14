CREATE TABLE IF NOT EXISTS cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    country VARCHAR(50) NOT NULL,
    latitude NUMERIC(9,6),
    longitude NUMERIC(9,6),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS weather_readings (
    id SERIAL PRIMARY KEY,
    city_id INTEGER NOT NULL,
    temperature NUMERIC(5,2) NOT NULL,
    feels_like NUMERIC(5,2),
    humidity INTEGER,
    condition VARCHAR(50),
    collected_at TIMESTAMP NOT NULL,

    CONSTRAINT fk_weather_city
        FOREIGN KEY (city_id)
        REFERENCES cities(id)
        ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_weather_city_date
    ON weather_readings (city_id, collected_at);

CREATE TABLE IF NOT EXISTS alerts (
    id SERIAL PRIMARY KEY,
    city_id INTEGER NOT NULL,
    alert_type VARCHAR(50) NOT NULL,
    threshold NUMERIC(5,2) NOT NULL,
    actual_value NUMERIC(5,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_alert_city
        FOREIGN KEY (city_id)
        REFERENCES cities(id)
        ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_alert_city_date
    ON alerts (city_id, created_at);


CREATE TABLE IF NOT EXISTS daily_summary (
    id SERIAL PRIMARY KEY,
    city_id INTEGER NOT NULL,
    date DATE NOT NULL,
    temp_min NUMERIC(5,2),
    temp_max NUMERIC(5,2),
    temp_avg NUMERIC(5,2),
    alerts_count INTEGER DEFAULT 0,

    CONSTRAINT fk_summary_city
        FOREIGN KEY (city_id)
        REFERENCES cities(id)
        ON DELETE CASCADE,

    CONSTRAINT uq_city_date
        UNIQUE (city_id, date)
);

CREATE INDEX IF NOT EXISTS idx_summary_city_date
    ON daily_summary (city_id, date);
