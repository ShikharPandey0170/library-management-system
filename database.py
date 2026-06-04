import pymysql as sql

def setup_database():
    try:
        connection = sql.connect(
            host="localhost",
            user="root",
            password="root"
        )

        cursor = connection.cursor()

        cursor.execute("CREATE DATABASE IF NOT EXISTS library;")
        cursor.execute("USE library;")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS books(
            book_id INT AUTO_INCREMENT PRIMARY KEY, 
            title VARCHAR(255) NOT NULL,
            author VARCHAR(255) NOT NULL,
            genre VARCHAR(50),
            quantity INT DEFAULT 1
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS members(
            member_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            phone VARCHAR(20),
            email VARCHAR(255)
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS borrow_records(
            record_id INT AUTO_INCREMENT PRIMARY KEY,
            member_id INT,
            book_id INT,
            borrow_date DATE,
            return_date DATE,
            FOREIGN KEY (member_id) REFERENCES members(member_id),
            FOREIGN KEY (book_id) REFERENCES books(book_id)
        );
        """)

        connection.commit()
        print("Database connected successfully!")

        cursor.close()
        connection.close()

    except sql.Error as e:
        print(f"Error setting up database: {e}")


def get_connection():
    try:
        connection = sql.connect(
            host="localhost",
            user="root",
            password="root",
            database="library"
        )
        return connection

    except sql.Error as e:
        print(f"Error connecting to database: {e}")
        return None