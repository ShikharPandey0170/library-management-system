#Borrowing Functions
from database import get_connection

def borrow_book(member_id, book_id):
    connection = None
    cursor = None
    
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT quantity FROM books WHERE book_id = %s;", (book_id,))
        
        row=cursor.fetchone()
        if row is None:
            print("Book not found.")
            return
        quantity = row[0]
        
        if quantity > 0:
            cursor.execute("INSERT INTO borrow_records (member_id, book_id, borrow_date) VALUES (%s, %s, CURDATE())", (member_id, book_id))
            cursor.execute("UPDATE books SET quantity = quantity - 1 WHERE book_id = %s;", (book_id,))
            connection.commit()
            print("Book borrowed successfully!")
        else:
            print("Sorry, this book is currently unavailable.")
    
    except Exception as e:
        if connection:
            connection.rollback()
        print(f"Error borrowing book: {e}")
    
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def return_book(record_id):
    connection = None
    cursor = None
    
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT book_id, return_date FROM borrow_records WHERE record_id = %s;", (record_id,))
        
        row = cursor.fetchone()
        if row is None:
            print("Borrow record not found.")
            return
        if row[1] is not None:
            print("This book has already been returned.")
            return
        book_id = row[0]

        cursor.execute("UPDATE borrow_records SET return_date = CURDATE() WHERE record_id = %s;", (record_id,))
        cursor.execute("UPDATE books SET quantity = quantity + 1 WHERE book_id = %s;", (book_id,))
        connection.commit()
        print("Book returned successfully!")
    
    except Exception as e:
        if connection:
            connection.rollback()
        print(f"Error returning book: {e}")
    
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
    
def view_borrow_records():
    connection = None
    cursor = None
   
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""
                       SELECT br.record_id, 
                       m.name, 
                       b.title, 
                       br.borrow_date, 
                       br.return_date
                       FROM borrow_records br
                       JOIN members m ON br.member_id = m.member_id
                       JOIN books b ON br.book_id = b.book_id;""")
        records = cursor.fetchall()
        if not records:
            print("No borrow records found.")
            return
        for record in records:
            record_id, member_name, book_title, borrow_date, return_date = record
            borrow_date_str = borrow_date.strftime("%d %B %Y")
            return_date_str = return_date.strftime("%d %B %Y") if return_date else "Not returned"
            print(f"Record ID: {record_id}\nMember: {member_name}\nBook: {book_title}\nBorrow Date: {borrow_date_str}\nReturn Date: {return_date_str}")
            print("-" * 40)
    except Exception as e:
        print(f"Error viewing borrow records: {e}")
    
    finally:        
        if cursor:
            cursor.close()
        if connection:
            connection.close()