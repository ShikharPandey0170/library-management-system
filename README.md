# Library Management System

A Command-Line Interface (CLI) application built with **Python** and **MySQL** for managing basic library operations. The system allows users to manage books and members, borrow and return books, and maintain borrowing records with automatic inventory updates.

This project uses a **modular file structure**, where database setup, book functions, member functions, borrowing functions, and the main menu are separated into different Python files for better readability, maintainability, and collaborative development.

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

### Borrowing and Return System

* Borrow books for registered members
* Check book quantity before borrowing
* Automatically reduce book quantity when borrowed
* Return borrowed books
* Automatically increase book quantity after return
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
* Git and GitHub

---

## Project Structure

```text
library-management-system/
│
├── main.py
├── database.py
├── book_functions.py
├── member_functions.py
├── borrow_functions.py
├── requirements.txt
├── README.md
├── .gitignore
└── .gitattributes
```

### File Description

| File                  | Description                                                                                           |
| --------------------- | ----------------------------------------------------------------------------------------------------- |
| `main.py`             | Contains the main menu and controls the program flow                                                  |
| `database.py`         | Handles MySQL connection, database creation, and table creation                                       |
| `book_functions.py`   | Contains book-related operations such as adding, viewing, searching, updating, and deleting books     |
| `member_functions.py` | Contains member-related operations such as adding, viewing, searching, updating, and deleting members |
| `borrow_functions.py` | Contains book borrowing, book returning, and borrow-record viewing functions                          |
| `requirements.txt`    | Contains required Python packages                                                                     |
| `README.md`           | Contains project documentation                                                                        |

---

## Database Structure

### Database Name

```sql
library
```

The database is created automatically by the application if it does not already exist.

---

### Books Table

| Column     | Type                             | Description                |
| ---------- | -------------------------------- | -------------------------- |
| `book_id`  | INT, Primary Key, Auto Increment | Unique ID for each book    |
| `title`    | VARCHAR(255), NOT NULL           | Book title                 |
| `author`   | VARCHAR(255), NOT NULL           | Book author                |
| `genre`    | VARCHAR(50)                      | Book category or genre     |
| `quantity` | INT, DEFAULT 1                   | Number of available copies |

---

### Members Table

| Column      | Type                             | Description               |
| ----------- | -------------------------------- | ------------------------- |
| `member_id` | INT, Primary Key, Auto Increment | Unique ID for each member |
| `name`      | VARCHAR(255), NOT NULL           | Member name               |
| `phone`     | VARCHAR(20)                      | Member phone number       |
| `email`     | VARCHAR(255)                     | Member email address      |

---

### Borrow Records Table

| Column        | Type                             | Description                      |
| ------------- | -------------------------------- | -------------------------------- |
| `record_id`   | INT, Primary Key, Auto Increment | Unique ID for each borrow record |
| `member_id`   | INT, Foreign Key                 | References `members.member_id`   |
| `book_id`     | INT, Foreign Key                 | References `books.book_id`       |
| `borrow_date` | DATE                             | Date when the book was borrowed  |
| `return_date` | DATE                             | Date when the book was returned  |

---

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ShikharPandey0170/library-management-system.git
cd library-management-system
```

---

### 2. Install Dependencies

Install the required Python package using `requirements.txt`:

```bash
pip install -r requirements.txt
```

Or install PyMySQL directly:

```bash
pip install pymysql
```

---

### 3. Configure MySQL

Make sure MySQL is installed and running on your system.

Update the MySQL credentials in `database.py` according to your local MySQL setup:

```python
connection = sql.connect(
    host="localhost",
    user="root",
    password="your_password"
)
```

The project uses a MySQL database named:

```sql
library
```

---

### 4. Run the Application

Run the project using:

```bash
python main.py
```

The application will automatically:

* Create the `library` database if it does not already exist
* Create the required tables if they do not already exist
* Launch the CLI menu

---

## Main Menu

```text
Library Management System

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

## How the System Works

1. The program starts from `main.py`.
2. `main.py` calls the database setup function from `database.py`.
3. The database and required tables are created automatically if they do not already exist.
4. The user selects an option from the CLI menu.
5. Based on the selected option:

   * Book operations are handled by `book_functions.py`
   * Member operations are handled by `member_functions.py`
   * Borrowing and return operations are handled by `borrow_functions.py`
6. Data is stored permanently in the MySQL database.

---

## Sample Learning Outcomes

This project demonstrates:

* Python functions
* Modular programming
* MySQL database design
* CRUD operations
* SQL JOIN operations
* Foreign key relationships
* Database connectivity using PyMySQL
* Menu-driven CLI development
* Basic exception handling
* Collaborative GitHub workflow

---

## Future Improvements

* Login and authentication system
* Admin and librarian roles
* Fine calculation for late returns
* Due date tracking
* Book availability reports
* Better input validation
* Prevent deletion of books or members with borrowing history
* Prevent duplicate return of the same borrow record
* Handle invalid book IDs, member IDs, and record IDs safely
* Export borrow records to CSV
* Search books by genre
* Graphical User Interface using Tkinter
* Web version using Flask or Django

---

## Authors

* Shikhar Pandey
* Prisha Gupta

Project developed collaboratively using **Python** and **MySQL**.
