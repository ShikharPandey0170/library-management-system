#Member Functions
import pymysql

from database import get_connection

def add_member(name, phone, email):
    connection = None
    cursor = None
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO members (name, phone, email) VALUES (%s, %s, %s)", (name, phone, email))
        connection.commit()
        print("Member added successfully!")
    except pymysql.err.IntegrityError as e:
        if e.args[0] == 1062:  # Duplicate entry error code
            print("Error: A member with this email already exists.")
        else:
            print(f"Database integrity error: {e}")
    except Exception as e:
        print(f"Error adding member: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def view_members():
    connection = None
    cursor = None
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM members;")
        members = cursor.fetchall()
        if not members:
            print("No members found.")
        for member in members:
            print(member)
    except Exception as e:
        print(f"Error viewing members: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def search_members(keyword):
    connection = None
    cursor = None
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM members WHERE name LIKE %s OR phone LIKE %s OR email LIKE %s;", ('%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%'))
        members = cursor.fetchall()
    
        if not members:
            print("No members found matching the keyword.")
    
        for member in members:
            print(member)
    except Exception as e:
        print(f"Error searching members: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def update_member(member_id, name=None, phone=None, email=None):
    if name is None and phone is None and email is None:
        print("Nothing to update.")
        return
    connection = None
    cursor = None
    try:
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
    except Exception as e:
        if connection:
            connection.rollback()
        print(f"Error updating member: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def delete_member(member_id):
    connection = None
    cursor = None
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM members WHERE member_id = %s;", (member_id,))
        connection.commit()
        if cursor.rowcount == 0:
            print(f"No member found with the ID {member_id}.")
        else:
            print("Member deleted successfully!")
    except Exception as e:
        print(f"Error deleting member: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()