import sqlite3

class DatabaseHelper:
    def __init__(self, db_name="data.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()
        self.add_average_temperature_column()

    def create_tables(self):
        with self.conn:
            self.conn.execute('''CREATE TABLE IF NOT EXISTS weather_data (
                city TEXT PRIMARY KEY,
                temperature REAL,
                feels_like REAL
            )''')

    def add_average_temperature_column(self):
        cursor = self.conn.cursor()
        cursor.execute("PRAGMA table_info(weather_data)")
        columns = [col[1] for col in cursor.fetchall()]

        if "average_temperature" not in columns:
            with self.conn:
                self.conn.execute("ALTER TABLE weather_data ADD COLUMN average_temperature REAL")

    def insert_weather_data(self, city, temperature, feels_like):
        average_temperature = (temperature + feels_like) / 2
        with self.conn:
            self.conn.execute(
                '''INSERT INTO weather_data (city, temperature, feels_like, average_temperature) 
                VALUES (?, ?, ?, ?)
                ON CONFLICT(city) DO UPDATE 
                SET temperature = excluded.temperature, 
                    feels_like = excluded.feels_like, 
                    average_temperature = excluded.average_temperature''',
                (city, temperature, feels_like, average_temperature)
            )

    def get_weather_data(self, city):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM weather_data WHERE city = ?", (city,))
        data = cursor.fetchone()
        if data:
            return {
                "city": data[0],
                "temperature": data[1],
                "feels_like": data[2],
                "average_temperature": data[3]
            }
        return None

