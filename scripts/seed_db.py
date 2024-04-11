import csv
import os
import psycopg2


def _seed_data():
    conn = _get_connection()
    cursor = conn.cursor()

    _create_table(cursor)
    rows = _read_csvs()
    _actually_seed_data(cursor, rows)

    conn.commit()
    conn.close()


def _create_table(cursor):
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS trip_data (id SERIAL PRIMARY KEY, pickup_datetime TIMESTAMP, passenger_count INT);"
    )


def _actually_seed_data(cursor, rows):
    for row in rows:
        datetime, passenger_count = row
        cursor.execute(
            f"INSERT INTO trip_data (pickup_datetime, passenger_count) VALUES ('{datetime}', {passenger_count or 'NULL'});"
        )


def _read_csvs():
    directory = "data"
    files = os.listdir(directory)
    values = []
    for file in files:
        file_path = os.path.join(directory, file)
        print(f"Reading '{file}'...")
        with open(file_path, "r") as csv_file:
            csv_reader = csv.reader(csv_file)

            titles = next(csv_reader)
            pickup_datetime_index = titles.index("pickup_datetime")
            passenger_count_index = titles.index("passenger_count")

            for row in csv_reader:
                values.append((row[pickup_datetime_index], row[passenger_count_index]))
    return values


def _get_connection():
    return psycopg2.connect(
        host=os.environ["DB_HOST"],
        database=os.environ["DB_DATABASE_NAME"],
        user=os.environ["DB_USERNAME"],
        password=os.environ["DB_PASSWORD"],
    )


if __name__ == "__main__":
    print("Seeding db")
    _seed_data()
