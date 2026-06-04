#Borrowing Functions
from database import get_connection

def borrow_book(member_id, book_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT quantity FROM books WHERE book_id = %s;", (book_id,))
    quantity = cursor.fetchone()[0]
    if quantity > 0:
        cursor.execute("INSERT INTO borrow_records (member_id, book_id, borrow_date) VALUES (%s, %s, CURDATE())", (member_id, book_id))
        cursor.execute("UPDATE books SET quantity = quantity - 1 WHERE book_id = %s;", (book_id,))
        connection.commit()
        print("Book borrowed successfully!")
    else:
        print("Sorry, this book is currently unavailable.")
    
    cursor.close()
    connection.close()

def return_book(record_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT book_id FROM borrow_records WHERE record_id = %s;", (record_id,))
    book_id = cursor.fetchone()[0]
    cursor.execute("UPDATE borrow_records SET return_date = CURDATE() WHERE record_id = %s;", (record_id,))
    cursor.execute("UPDATE books SET quantity = quantity + 1 WHERE book_id = %s;", (book_id,))
    connection.commit()
    print("Book returned successfully!")

    cursor.close()
    connection.close()

def view_borrow_records():
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
    for record in records:
        print(record)

    cursor.close()
    connection.close()