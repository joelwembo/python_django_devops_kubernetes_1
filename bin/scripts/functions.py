import pandas as pd
import psycopg2
from functools import partial

# Database connection details
DB_NAME = 'db4'
DB_USER = 'postgres'
DB_PASSWORD = 'postgres'
DB_HOST = 'localhost'
DB_PORT = 5432

# Function to establish a connection to the PostgreSQL database
def connect_to_db(db_name, db_user, db_password, db_host, db_port):
    try:
        conn = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        print("Database connection established")
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

# Partial function to reuse the connection parameters
connect_db = partial(connect_to_db, DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT)

# Function to fetch data from a specified table
def fetch_data_from_table(table_name):
    conn = connect_db()
    if conn:
        query = f"SELECT * FROM {table_name};"
        try:
            # Fetch data into a pandas DataFrame
            df = pd.read_sql(query, conn)
            print(f"Data from table {table_name}:")
            print(df)
        except Exception as e:
            print(f"Error fetching data from table {table_name}: {e}")
        finally:
            conn.close()
    else:
        print("Failed to connect to the database.")

# Example usage
if __name__ == '__main__':
    table_name = 'public."Accounts"'  # Replace with your table name
    fetch_data_from_table(table_name)
