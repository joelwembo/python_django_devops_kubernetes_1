import pandas as pd
from sqlalchemy import create_engine
from functools import partial

# Database connection details
DB_NAME = 'db4'
DB_USER = 'postgres'
DB_PASSWORD = 'postgres'
DB_HOST = 'localhost'
DB_PORT = 5432

# Function to create SQLAlchemy engine
def create_db_engine(db_name, db_user, db_password, db_host, db_port):
    try:
        # PostgreSQL connection string for SQLAlchemy
        db_url = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
        engine = create_engine(db_url)
        print("Database engine created successfully")
        return engine
    except Exception as e:
        print(f"Error creating the database engine: {e}")
        return None

# Partial function to reuse the connection parameters
get_engine = partial(create_db_engine, DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT)

# Function to fetch data from a specified table
def fetch_data_from_table(table_name):
    engine = get_engine()
    if engine:
        query = f"SELECT * FROM {table_name};"
        try:
            # Fetch data into a pandas DataFrame using SQLAlchemy engine
            df = pd.read_sql(query, engine)
            print(f"Data from table {table_name}:")
            print(df)
        except Exception as e:
            print(f"Error fetching data from table {table_name}: {e}")
        finally:
            engine.dispose()
    else:
        print("Failed to create the database engine.")

# Example usage
if __name__ == '__main__':
    table_name = 'auth_user'  # Replace with your table name
    fetch_data_from_table(table_name)
