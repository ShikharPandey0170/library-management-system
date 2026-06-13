#Book Functions
from dataclasses import fields
from database import setup_database
from database import get_connection

def add_book(title, author, genre, quantity):
    title = title.strip()
    author = author.strip()
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
            print(f"\n⚠️ Notice: '{title}' by {author} already exists in the library.")
            print(f"Current stock quantity: {existing_book[1]}")
            user_choice = input(f"Do you want to add {quantity} more to the existing stock? (yes/no): ").strip().lower()
           
            if user_choice in ['yes', 'y']:
                new_qty = existing_book[1] + quantity
                update_sql = "UPDATE books SET quantity = %s WHERE book_id = %s"
                cursor.execute(update_sql, (new_qty, existing_book[0]))
                connection.commit()
                print(f"✔️ Stock updated! New total quantity: {new_qty}")
            else:
                print("❌ Operation cancelled. No changes were made to the database.")
                
        else:
            insert_sql = "INSERT INTO books (title, author, genre, quantity) VALUES (%s, %s, %s, %s)"
            cursor.execute(insert_sql, (title, author, genre, quantity))
            connection.commit()
            print(f"\n✔️ Success: New book '{title}' added to the library inventory!")
          
        
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
            return
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
    if connection is None:
        return

    cursor = None
    try:
        cursor = connection.cursor()
        
        # 1. Fetch the book first to show the user what they are managing
        cursor.execute("SELECT title, author, quantity FROM books WHERE book_id = %s;", (book_id,))
        book = cursor.fetchone()
        
        if not book:
            print(f"\n⚠️ Warning: No book found with ID {book_id}.")
            return
            
        # 👑 Corrected indices: book[0] is title, book[1] is author, book[2] is quantity
        print(f"\n📝 Target Book Selected: '{book[0]}' by {book[1]} (Current Stock: {book[2]})")
        print("-" * 60)
        print("1. 📉 Set Quantity to 0 (Keeps the Book ID active for future stock)")
        print("2. 💥 Permanently Delete (Wipes record entirely, creating an ID gap)")
        
        choice = input("\n👉 Choose an option (1 or 2): ").strip()
        
        if choice == "1":
            cursor.execute("UPDATE books SET quantity = 0 WHERE book_id = %s;", (book_id,))
            connection.commit()
            print(f"\n✔️ Stock cleared! '{book[0]}' is now marked out of stock.")
            
       
        elif choice == "2":
            print(f"\n⚠️ WARNING: Wiping this row can break old borrow history logs.")
            print("💡 TIP: If you just misspelled something, consider using Option 4 from the Main Menu to 'Update' instead!")
            
            confirm = input(f"\nAre you absolutely sure you want to permanently delete this record? (yes/no): ").strip().lower()
            
            if confirm in ['yes', 'y']:
                cursor.execute("DELETE FROM books WHERE book_id = %s;", (book_id,))
                connection.commit()
                print(f"\n🗑️ Success: Book ID {book_id} completely removed from the database.")
            
            else:
                print("\n❌ Operation cancelled. No records were destroyed.")
                
        else:
            print("\n❌ Invalid selection. Returning to Main Menu.")

    except Exception as e:
        print(f"\n❌ Error processing delete request: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
  
