import os
import psycopg2

try:
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST", "127.0.0.1"),
        user=os.getenv("DB_USER", "esguser"),
        password=os.getenv("DB_PASSWORD", ""),
        dbname=os.getenv("DB_NAME", "esgdb"),
    )
    print("Success")
except Exception as e:
    print(f"Error args: {e.args}")
    print(f"pgerror: {getattr(e, 'pgerror', None)}")
