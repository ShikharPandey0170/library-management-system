#Member Functions
from database import get_connection

def add_member(name, phone, email):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("INSERT INTO members (name, phone, email) VALUES (%s, %s, %s)", (name, phone, email))
    connection.commit()

    print("Member added successfully!")
    cursor.close()
    connection.close()

def view_members():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM members;")
    members = cursor.fetchall()

    if not members:
        print("No members found.")

    for member in members:
        print(member)
    
    cursor.close()
    connection.close()
    
def search_members(keyword):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM members WHERE name LIKE %s OR email LIKE %s;", ('%' + keyword + '%', '%' + keyword + '%'))
    members = cursor.fetchall()
    
    if not members:
        print("No members found matching the keyword.")
    
    for member in members:
        print(member)

    cursor.close()
    connection.close()

def update_member(member_id, name=None, phone=None, email=None):
    connection = get_connection()
    cursor = connection.cursor()

    if name:
        cursor.execute("UPDATE members SET name = %s WHERE member_id = %s;", (name, member_id))
    if phone:
        cursor.execute("UPDATE members SET phone = %s WHERE member_id = %s;", (phone, member_id))
    if email:
        cursor.execute("UPDATE members SET email = %s WHERE member_id = %s;", (email, member_id))
    connection.commit()
    print("Member updated successfully!")
    cursor.close()
    connection.close()

def delete_member(member_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM members WHERE member_id = %s;", (member_id,))
    connection.commit()
    print("Member deleted successfully!")
    cursor.close()
    connection.close()