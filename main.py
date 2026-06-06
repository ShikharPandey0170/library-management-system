import sys
from book_functions import add_book, view_books, search_books, update_book, delete_book
from member_functions import add_member, view_members, search_members, update_member, delete_member
from borrow_functions import borrow_book, return_book, view_borrow_records

def print_menu():
    print("\n" + "═"*50)
    print("📚       LIBRARY MANAGEMENT SYSTEM DASHBOARD       📚")
    print("═"*50)
    
    print("\n🔹 [ BOOK MANAGEMENT ]")
    print("  1. ➕ Add Book")
    print("  2. 📖 View All Books")
    print("  3. 🔍 Search Books")
    print("  4. ✏️  Update Book")
    print("  5. 🗑️  Delete Book")
    
    print("\n🔹 [ MEMBER MANAGEMENT ]")
    print("  6. 👤 Register Member") 
    print("  7. 👥 View All Members")
    print("  8. 🔍 Search Members")
    print("  9. ✏️  Update Member")
    print("  10.🗑️  Remove Member")
    
    print("\n🔹 [ BORROW & RETURN SYSTEM ]")
    print("  11.📥 Borrow Book")
    print("  12.📤 Return Book")
    print("  13.📜 View Borrow History")
    
    print("\n🔹 [ SYSTEM ]")
    print("  14.❌ Exit Application")
    print("═"*50)

def safe_int_input(prompt):
   
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("⚠️ Invalid format. Please enter a valid numerical ID or quantity.")

# --- MAIN RUNNING LOOP ---
while True:
    print_menu()
    
    try:
        choice = int(input("\n👉 Enter your selection (1-14): "))
    except ValueError:
        print("\n❌ Invalid option. Please enter a number between 1 and 14.")
        continue

    print("\n" + "─"*50) # Section Divider line

    if choice == 1:
        print("📥 [ ADD NEW BOOK ]")
        title = input("Enter book title: ").strip()
        author = input("Enter book author: ").strip()
        genre = input("Enter book genre: ").strip()
        quantity = safe_int_input("Enter stock quantity: ")
        add_book(title, author, genre, quantity)
    
    elif choice == 2:
        view_books()

    elif choice == 3:
        print("🔍 [ SEARCH BOOK INVENTORY ]")
        keyword = input("Enter title or author keyword: ").strip()
        search_books(keyword)
    
    elif choice == 4:
        print("✏️ [ UPDATE BOOK DETAILS ]")
        book_id = safe_int_input("Enter book ID to modify: ")
        # Checking if they want to leave fields blank can be handled inside your input strings
        title = input("Enter new title (Leave blank to keep current): ").strip() or None
        author = input("Enter new author (Leave blank to keep current): ").strip() or None
        genre = input("Enter new genre (Leave blank to keep current): ").strip() or None
        
        qty_input = input("Enter new quantity (Leave blank to keep current): ").strip()
        quantity = int(qty_input) if qty_input.isdigit() else None
        
        update_book(book_id, title, author, genre, quantity)
    
    elif choice == 5:
        print("🗑️ [ REMOVE BOOK FROM INVENTORY ]")
        book_id = safe_int_input("Enter book ID to permanently delete: ")
        delete_book(book_id)
    
    elif choice == 6:
        print("👤 [ REGISTER NEW MEMBER ]")
        name = input("Enter member full name: ").strip()
        phone = input("Enter member phone number: ").strip()
        email = input("Enter member email address: ").strip()
        add_member(name, phone, email)
    
    elif choice == 7:
        view_members()
    
    elif choice == 8:
        print("🔍 [ SEARCH MEMBERS ]")
        keyword = input("Enter name or email keyword: ").strip()
        search_members(keyword)
    
    elif choice == 9:
        print("✏️ [ UPDATE MEMBER PROFILE ]")
        member_id = safe_int_input("Enter member ID to update: ")
        name = input("Enter new name (Leave blank to skip): ").strip() or None
        phone = input("Enter new phone (Leave blank to skip): ").strip() or None
        email = input("Enter new email (Leave blank to skip): ").strip() or None
        update_member(member_id, name, phone, email)
    
    elif choice == 10:
        print("🗑️ [ TERMINATE MEMBER ACCOUNT ]")
        member_id = safe_int_input("Enter member ID to remove: ")
        delete_member(member_id)
    
    elif choice == 11:
        print("📥 [ ISSUE BOOK TRANSACTION ]")
        member_id = safe_int_input("Enter borrowing Member ID: ")
        book_id = safe_int_input("Enter target Book ID: ")
        borrow_book(member_id, book_id)
    
    elif choice == 12:
        print("📤 [ RETURN BOOK TRANSACTION ]")
        record_id = safe_int_input("Enter transaction Borrow Record ID: ")
        return_book(record_id)
    
    elif choice == 13:
        print("------- Borrow/Return Records ------- ")
        view_borrow_records()
    
    elif choice == 14:
        print("\n🔒 Safely closing the Library Management Database. Goodbye!")
        print("═"*50 + "\n")
        sys.exit()

    else:
        print("\n❌ Choice out of bounds. Select an integer from 1 to 14.")