import pymysql as sql
def get_connection():
    try:
        connection = sql.connect(host='localhost', user='root', password='root',database='library')
        return connection
    except sql.Error as e:
        print(f"Error connecting to database: {e}")
        return None
