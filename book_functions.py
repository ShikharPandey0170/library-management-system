#Book Functions
from database import get_connection

def add_book(title, author, genre, quantity):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("INSERT INTO books (title, author, genre, quantity) VALUES (%s, %s, %s, %s)", (title, author, genre, quantity))
    connection.commit()
    print("Book added successfully!")

    cursor.close()
    connection.close()

def view_books():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM books;")
    books = cursor.fetchall()
    
    if not books:
        print("No books found.")

    for book in books:
        print(book)

    cursor.close()
    connection.close()

def search_books(keyword):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM books WHERE title LIKE %s OR author LIKE %s;", ('%' + keyword + '%', '%' + keyword + '%'))
    books = cursor.fetchall()
    
    if not books:
        print("No books found matching the keyword.")
    
    for book in books:
        print(book)
    
    cursor.close()
    connection.close()

def update_book(book_id, title=None, author=None, genre=None, quantity=None):
    connection = get_connection()
    cursor = connection.cursor()

    if title:
        cursor.execute("UPDATE books SET title = %s WHERE book_id = %s;", (title, book_id))
    if author:
        cursor.execute("UPDATE books SET author = %s WHERE book_id = %s;", (author, book_id))
    if genre:
        cursor.execute("UPDATE books SET genre = %s WHERE book_id = %s;", (genre, book_id))
    if quantity is not None:
        cursor.execute("UPDATE books SET quantity = %s WHERE book_id = %s;", (quantity, book_id))
    connection.commit()
    print("Book updated successfully!")

    cursor.close()
    connection.close()

def delete_book(book_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM books WHERE book_id = %s;", (book_id,))
    connection.commit()
    print("Book deleted successfully!")

    cursor.close()
    connection.close()