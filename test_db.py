import psycopg2
try:
    conn = psycopg2.connect(host='127.0.0.1', user='esguser', password='esgpass', dbname='esgdb')
    print("Success")
except Exception as e:
    print(f"Error args: {e.args}")
    print(f"pgerror: {getattr(e, 'pgerror', None)}")
