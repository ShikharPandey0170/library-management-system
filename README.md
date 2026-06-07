# 📚 Library Management System

A **Terminal-Based Library Management System** built using **Python** and **MySQL** that provides a complete solution for managing books, members, borrowing transactions, and inventory records.

The application follows a **modular functional programming architecture**, separating database operations, business logic, and CLI control into independent Python modules for improved readability, maintainability, and scalability.

---

## ✨ Features

## 📖 Book Management

The inventory module provides complete CRUD operations for managing books.

Features:

- Add new books
- View all available books
- Search books by title or author
- Update existing book details
- Delete books
- Maintain stock quantity

Additional handling:

- Prevents duplicate books using title-author validation
- Allows increasing quantity when the same book already exists
- Supports partial updates using dynamic field handling
- Provides safe deletion options

---

## 👥 Member Management

Manage library member profiles efficiently.

Features:

- Register new members
- View all members
- Search members by name or email
- Update member information
- Delete members

Database protection:

- Prevents duplicate emails using MySQL unique constraints
- Handles MySQL duplicate entry errors safely
- Uses rollback protection for failed operations

---

## 🔄 Borrow & Return System

A complete transaction-based lending system.

Features:

- Borrow books for registered members
- Check available quantity before borrowing
- Automatically decrease book stock
- Return previously borrowed books
- Automatically restore book quantity

Transaction safety:

- Prevents invalid return operations
- Uses database rollback on failures
- Maintains consistent inventory records

---

## 📜 Borrow Records

Tracks complete borrowing history.

Displays:

- Member details
- Book information
- Borrow date
- Return date

Uses SQL JOIN operations between:

```
borrow_records
        |
        |
     members
        |
        |
      books
```

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.x | Application development |
| MySQL | Database management |
| PyMySQL | Python-MySQL connection |
| SQL | Queries and relationships |
| Git/GitHub | Version control |

---

# 🏗️ Project Architecture

The project uses a modular functional programming design.

Each module handles a specific responsibility:

```
User
 |
 |
main.py
 |
 |
 +----------------------+
 |          |           |
Books   Members     Borrowing
 |          |           |
book_functions.py
member_functions.py
borrow_functions.py

 |
database.py

 |
MySQL Database
```

---

# 📂 Project Structure

```
library-management-system/

│
├── main.py
│
├── database.py
│
├── book_functions.py
│
├── member_functions.py
│
├── borrow_functions.py
│
├── requirements.txt
│
├── README.md
│
├── .gitignore
│
└── .gitattributes
```

---

# 📌 File Description

| File | Description |
|---|---|
| `main.py` | Controls CLI dashboard and program execution flow |
| `database.py` | Creates database, tables, and manages MySQL connections |
| `book_functions.py` | Handles book CRUD and inventory operations |
| `member_functions.py` | Handles member CRUD operations |
| `borrow_functions.py` | Handles borrowing, returning, and history records |
| `requirements.txt` | Required Python packages |
| `README.md` | Project documentation |

---

# 🗄️ Database Structure

Database Name:

```sql
library
```

The database is automatically created when the application starts.

Default MySQL configuration:

```
Host: localhost
User: root
Password: root
```

---

# 📚 Books Table

Table:

```sql
books
```

Structure:

| Column | Type | Constraint |
|---|---|---|
| book_id | INT | PRIMARY KEY AUTO_INCREMENT |
| title | VARCHAR(255) | NOT NULL |
| author | VARCHAR(255) | NOT NULL |
| genre | VARCHAR(50) | Book category |
| quantity | INT | CHECK(quantity >= 0) |

---

# 👤 Members Table

Table:

```sql
members
```

Structure:

| Column | Type | Constraint |
|---|---|---|
| member_id | INT | PRIMARY KEY AUTO_INCREMENT |
| name | VARCHAR(255) | NOT NULL |
| phone | VARCHAR(20) | UNIQUE |
| email | VARCHAR(255) | UNIQUE |

---

# 🔄 Borrow Records Table

Table:

```sql
borrow_records
```

Structure:

| Column | Type | Constraint |
|---|---|---|
| record_id | INT | PRIMARY KEY AUTO_INCREMENT |
| member_id | INT | FOREIGN KEY |
| book_id | INT | FOREIGN KEY |
| borrow_date | DATE | DEFAULT CURDATE() |
| return_date | DATE | NULL |

Relationships:

Member deletion:

```sql
ON DELETE CASCADE
```

Book deletion:

```sql
ON DELETE RESTRICT
```

---

# ⚙️ Installation & Setup

## 1. Clone Repository

```bash
git clone https://github.com/ShikharPandey0170/library-management-system.git

cd library-management-system
```

---

## 2. Install Dependencies

Using requirements file:

```bash
pip install -r requirements.txt
```

or:

```bash
pip install pymysql
```

---

## 3. Configure MySQL

Make sure MySQL Server is running.

Update credentials in:

```
database.py
```

Example:

```python
host="localhost"
user="root"
password="root"
```

---

## 4. Initialize Database

Run:

```bash
python database.py
```

The system automatically creates:

- Database
- Tables
- Constraints

---

## 5. Start Application

Run:

```bash
python main.py
```

---

# 🖥️ Main Menu

```
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

# 🔐 Error Handling & Safety Features

Implemented protections:

✅ Invalid input handling  
✅ Safe integer conversion  
✅ Duplicate record prevention  
✅ SQL constraint protection  
✅ Transaction rollback  
✅ Foreign key validation  
✅ Inventory consistency checks  

---

# 🎯 Learning Outcomes

This project demonstrates:

- Python modular programming
- Functional architecture
- Database connectivity
- CRUD implementation
- SQL relationships
- Foreign keys
- JOIN queries
- Exception handling
- Transaction management
- Git collaboration workflow

---

# 🚀 Future Improvements

- User authentication system
- Admin and librarian roles
- Fine calculation system
- Due-date tracking
- CSV report export
- Advanced search filters
- GUI version using Tkinter
- Web version using Flask/Django
- Improved input validation

---

# 🤝 Contribution Guide

Contributions are welcome!

Steps:

1. Fork the repository

2. Create a branch:

```bash
git checkout -b feature-name
```

3. Commit changes:

```bash
git commit -m "Added new feature"
```

4. Push:

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# 📜 License

This project is licensed under the MIT License.

You are free to use, modify, and distribute this project with proper attribution.

---

# 👨‍💻 Authors

**Shikhar Pandey**  
**Prisha Gupta**

Developed collaboratively using:

🐍 Python  
🗄️ MySQL  
🔗 PyMySQL  

---

⭐ If you found this project useful, consider giving it a star!
