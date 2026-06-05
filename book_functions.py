#Book Functions
from dataclasses import fields
from database import setup_database
from database import get_connection

def add_book(title, author, genre, quantity):
    connection = get_connection()
    if connection is None:
        return

    cursor = None
    try:
        cursor = connection.cursor()
        check_sql = "SELECT book_id, quantity FROM books WHERE title = %s AND author = %s"
        cursor.execute(check_sql, (title, author))
        existing_book = cursor.fetchone()

        if existing_book:
            new_qty = existing_book[4] + quantity 
            update_sql = "UPDATE books SET quantity = %s WHERE book_id = %s"
            cursor.execute(update_sql, (new_qty, existing_book[0])) 
            print(f"\n✔️ Book already exists. Updated quantity to {new_qty}.")
        else:
            insert_sql = "INSERT INTO books (title, author, genre, quantity) VALUES (%s, %s, %s, %s)"
            cursor.execute(insert_sql, (title, author, genre, quantity))
            print("\n✔️ New book added successfully!")
            
        connection.commit()
    except Exception as e:
        print(f"\n❌ Error adding/updating book: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def view_books():
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM books;")
        books = cursor.fetchall()
    
        if not books:
            print("No books found.")
            return
    
        print("\n ------- Library Inventory ------- ")
        for book in books:
            print(book)
    except Exception as e:
        print(f"\n❌ Error fetching books: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()

def search_books(keyword):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM books WHERE title LIKE %s OR author LIKE %s;", ('%' + keyword + '%', '%' + keyword + '%'))
        books = cursor.fetchall()
    
        if not books:
            print("No books found matching the keyword.")
    
        for book in books:
            print(book)
    
    except Exception as e:
        print(f"\n❌ Error searching books: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()

def update_book(book_id, title=None, author=None, genre=None, quantity=None):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        fields = [title, author, genre, quantity]
    
        if not any(fields):
            print("\n⚠️ No fields provided for update.")
            return
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

       
    
    except Exception as e:
        print(f"\n❌ Error updating book: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()

def delete_book(book_id):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM books WHERE book_id = %s;", (book_id,))
        connection.commit()
        print(f"\n Book ID {book_id} deleted successfully!")
    except Exception as e:
        print(f"\n❌ Error deleting book: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()
  
# --- LOCAL TESTING BLOCK ---
if __name__ == "__main__":
    print("--- Starting Database Function Test ---")
    
    # 1. Test Adding a Book
    add_book("Twisted Games", "Ana Huang", "Fiction", 5)
    add_book("The Hobbit", "J.R.R. Tolkien", "Fantasy", 3)
    
    # 2. Test Viewing all Books
    print("\nTesting: View all books")
    view_books()
    
    # 3. Test Searching for a Book
    print("\nTesting: Search functionality")
    search_books("Ana")
    
    # 4. Test Updating (Let's change Harry Potter's quantity to 10)
    # Note: Check your printed database list to confirm Harry Potter's book_id matches!
    print("\nTesting: Update book ID 1")
    update_book(book_id=1, quantity=10)
    
    
    # 5. Check changes
    view_books()