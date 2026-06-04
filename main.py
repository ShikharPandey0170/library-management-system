#main.py
from book_functions import add_book, view_books, search_books, update_book, delete_book
from member_functions import add_member, view_members, search_members, update_member, delete_member
from borrow_functions import borrow_book, return_book, view_borrow_records

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
        title = input("Enter new title: ")
        author = input("Enter new author: ")
        genre = input("Enter new genre: ")
        quantity = int(input("Enter new quantity: "))
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
        name = input("Enter new name: ")
        phone = input("Enter new phone: ")
        email = input("Enter new email: ")
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