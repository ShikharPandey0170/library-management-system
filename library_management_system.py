import pymysql as sql
connection = sql.connect(host='localhost', user='root', password='root')
cursor = connection.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS library;")   
cursor.execute("USE library;")
print("Database connected successfully!")
cursor.execute("""CREATE TABLE IF NOT EXISTS books(
               book_id INT AUTO_INCREMENT PRIMARY KEY, 
               title VARCHAR(255) NOT NULL,
               author VARCHAR(255) NOT NULL,
               genre VARCHAR(50),
               quantity INT DEFAULT 1);""")
cursor.execute("""CREATE TABLE IF NOT EXISTS members(
               member_id INT AUTO_INCREMENT PRIMARY KEY,
               name VARCHAR(255) NOT NULL,
               phone VARCHAR(20),
               email VARCHAR(255));""")
cursor.execute("""CREATE TABLE IF NOT EXISTS borrow_records(
               record_id INT AUTO_INCREMENT PRIMARY KEY,
               member_id INT,
               book_id INT,
               borrow_date DATE,
               return_date DATE,
               FOREIGN KEY (member_id) REFERENCES members(member_id),
               FOREIGN KEY (book_id) REFERENCES books(book_id));""")
#Book Functions
def add_book(title, author, genre, quantity):
    cursor.execute("INSERT INTO books (title, author, genre, quantity) VALUES (%s, %s, %s, %s)", (title, author, genre, quantity))
    connection.commit()
    print("Book added successfully!")
def view_books():
    cursor.execute("SELECT * FROM books;")
    books = cursor.fetchall()
    
    if not books:
        print("No books found.")

    for book in books:
        print(book)
def search_books(keyword):
    cursor.execute("SELECT * FROM books WHERE title LIKE %s OR author LIKE %s;", ('%' + keyword + '%', '%' + keyword + '%'))
    books = cursor.fetchall()
    
    if not books:
        print("No books found matching the keyword.")
    
    for book in books:
        print(book)
def update_book(book_id, title=None, author=None, genre=None, quantity=None):
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
def delete_book(book_id):
    cursor.execute("DELETE FROM books WHERE book_id = %s;", (book_id,))
    connection.commit()
    print("Book deleted successfully!")
#Member Functions
def add_member(name, phone, email):
    cursor.execute("INSERT INTO members (name, phone, email) VALUES (%s, %s, %s)", (name, phone, email))
    connection.commit()
    print("Member added successfully!")
def view_members():
    cursor.execute("SELECT * FROM members;")
    members = cursor.fetchall()

    if not members:
        print("No members found.")

    for member in members:
        print(member)
def search_members(keyword):
    cursor.execute("SELECT * FROM members WHERE name LIKE %s OR email LIKE %s;", ('%' + keyword + '%', '%' + keyword + '%'))
    members = cursor.fetchall()
    
    if not members:
        print("No members found matching the keyword.")
    
    for member in members:
        print(member)
def update_member(member_id, name=None, phone=None, email=None):
    if name:
        cursor.execute("UPDATE members SET name = %s WHERE member_id = %s;", (name, member_id))
    if phone:
        cursor.execute("UPDATE members SET phone = %s WHERE member_id = %s;", (phone, member_id))
    if email:
        cursor.execute("UPDATE members SET email = %s WHERE member_id = %s;", (email, member_id))
    connection.commit()
    print("Member updated successfully!")
def delete_member(member_id):
    cursor.execute("DELETE FROM members WHERE member_id = %s;", (member_id,))
    connection.commit()
    print("Member deleted successfully!")
#Borrowing Functions
def borrow_book(member_id, book_id):
    cursor.execute("SELECT quantity FROM books WHERE book_id = %s;", (book_id,))
    quantity = cursor.fetchone()[0]
    if quantity > 0:
        cursor.execute("INSERT INTO borrow_records (member_id, book_id, borrow_date) VALUES (%s, %s, CURDATE())", (member_id, book_id))
        cursor.execute("UPDATE books SET quantity = quantity - 1 WHERE book_id = %s;", (book_id,))
        connection.commit()
        print("Book borrowed successfully!")
    else:
        print("Sorry, this book is currently unavailable.")
def return_book(record_id):
    cursor.execute("SELECT book_id FROM borrow_records WHERE record_id = %s;", (record_id,))
    book_id = cursor.fetchone()[0]
    cursor.execute("UPDATE borrow_records SET return_date = CURDATE() WHERE record_id = %s;", (record_id,))
    cursor.execute("UPDATE books SET quantity = quantity + 1 WHERE book_id = %s;", (book_id,))
    connection.commit()
    print("Book returned successfully!")
def view_borrow_records():
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
#Main Menu
while True:
    print("\n\tLibrary Management System")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Books")
    print("4. Update Book")
    print("5. Delete Book")
    print("6. Add Member")
    print("7. View Members")
    print("8. Search Members")
    print("9. Update Member")
    print("10. Delete Member")
    print("11. Borrow Book")
    print("12. Return Book")
    print("13. View Borrow Records")
    print("14. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        genre = input("Enter book genre: ")
        quantity = int(input("Enter quantity: "))
        add_book(title, author, genre, quantity)
    
    elif choice == 2:
        view_books()

    elif choice == 3:
        keyword = input("Enter keyword to search: ")
        search_books(keyword)
    
    elif choice == 4:
        book_id = int(input("Enter book ID to update: "))
        title = input("Enter new title (leave blank to keep unchanged): ")
        author = input("Enter new author (leave blank to keep unchanged): ")
        genre = input("Enter new genre (leave blank to keep unchanged): ")
        quantity_input = input("Enter new quantity (leave blank to keep unchanged): ")
        quantity = int(quantity_input) if quantity_input else None
        update_book(book_id, title, author, genre, quantity)
    
    elif choice == 5:
        book_id = int(input("Enter book ID to delete: "))
        delete_book(book_id)
    
    elif choice == 6:
        name = input("Enter member name: ")
        phone = input("Enter member phone: ")
        email = input("Enter member email: ")
        add_member(name, phone, email)
    
    elif choice == 7:
        view_members()
    
    elif choice == 8:
        keyword = input("Enter keyword to search: ")
        search_members(keyword)
    
    elif choice == 9:
        member_id = int(input("Enter member ID to update: "))
        name = input("Enter new name (leave blank to keep unchanged): ")
        phone = input("Enter new phone (leave blank to keep unchanged): ")
        email = input("Enter new email (leave blank to keep unchanged): ")
        update_member(member_id, name, phone, email)
    
    elif choice == 10:
        member_id = int(input("Enter member ID to delete: "))
        delete_member(member_id)
    
    elif choice == 11:
        member_id = int(input("Enter member ID: "))
        book_id = int(input("Enter book ID: "))
        borrow_book(member_id, book_id)
    
    elif choice == 12:
        record_id = int(input("Enter borrow record ID: "))
        return_book(record_id)
    
    elif choice == 13:
        view_borrow_records()
    
    elif choice == 14:
        print("Closing the system.")
        break

    else:
        print("Invalid choice. Please try again.")