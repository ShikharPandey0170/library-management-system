# Library Management System

A Command-Line Interface (CLI) application built with Python and MySQL for managing library operations. The system allows librarians to manage books and members, issue and return books, and maintain borrowing records with automatic inventory updates.

---

## Features

### Book Management

* Add new books
* View all books
* Search books by title or author
* Update book details
* Delete books from the database

### Member Management

* Register new members
* View all members
* Search members by name or email
* Update member details
* Delete members from the database

### Borrowing & Return System

* Borrow books for registered members
* Automatic quantity reduction when a book is borrowed
* Return books and automatically restock inventory
* Maintain borrowing history records

### Borrow Records

* View complete borrowing transaction history
* Display member names, book titles, borrow dates, and return dates
* Uses SQL JOIN operations for detailed record tracking

---

## Technologies Used

* Python 3
* MySQL
* PyMySQL

---

## Database Structure

### Books Table

| Column   | Type              |
| -------- | ----------------- |
| book_id  | INT (Primary Key) |
| title    | VARCHAR(255)      |
| author   | VARCHAR(255)      |
| genre    | VARCHAR(50)       |
| quantity | INT               |

### Members Table

| Column    | Type              |
| --------- | ----------------- |
| member_id | INT (Primary Key) |
| name      | VARCHAR(255)      |
| phone     | VARCHAR(20)       |
| email     | VARCHAR(255)      |

### Borrow Records Table

| Column      | Type              |
| ----------- | ----------------- |
| record_id   | INT (Primary Key) |
| member_id   | INT (Foreign Key) |
| book_id     | INT (Foreign Key) |
| borrow_date | DATE              |
| return_date | DATE              |

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/library-management-system-python-mysql.git
cd library-management-system-python-mysql
```

### 2. Install Dependencies

```bash
pip install pymysql
```

### 3. Configure MySQL

Update the database credentials in the source code:

```python
connection = sql.connect(
    host="localhost",
    user="root",
    password="your_password"
)
```

### 4. Run the Application

```bash
python library_management_system.py
```

The application will automatically:

* Create the database if it does not exist
* Create required tables
* Launch the CLI menu

---

## Main Menu

```text
1. Add Book
2. View Books
3. Search Books
4. Update Book
5. Delete Book
6. Add Member
7. View Members
8. Search Members
9. Update Member
10. Delete Member
11. Borrow Book
12. Return Book
13. View Borrow Records
14. Exit
```

---

## Sample Learning Outcomes

This project demonstrates:

* Python Functions
* MySQL Database Design
* CRUD Operations
* SQL Joins
* Foreign Keys
* Exception Handling
* Database Connectivity using PyMySQL
* Menu-Driven CLI Development

---

## Future Improvements

* Login and Authentication System
* Fine Calculation for Late Returns
* Due Date Tracking
* Book Availability Reports
* Input Validation Enhancements
* Export Records to CSV
* Modular File Structure
* Graphical User Interface (GUI)

---

## Author

Shikhar Pandey
Prisha Gupta

Project developed collaboratively using Python and MYSQL.
