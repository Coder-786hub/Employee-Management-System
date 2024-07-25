import mysql.connector
from tkinter import messagebox

def create_database():
    try:
        connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Aftab@786"
        )

        cursor=connection.cursor()
        
    except:
        messagebox.showerror("Error","Something Went wrong, Please open mysql app before running again")
        return
    
    databse_query="CREATE DATABASE IF NOT EXISTS EMPLOYEE_MANAGEMENT_SYSTEM"
    cursor.execute(databse_query)
    cursor.close()
    connection.close()

def create_table():
    try:
        connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Aftab@786",
            database="EMPLOYEE_MANAGEMENT_SYSTEM"
        )   

        cursor=connection.cursor()
    except:
        messagebox.showerror("Error","Mysql Databse Error Check Manually")
        return
    
    table_query="CREATE TABLE IF NOT EXISTS EMPLOYEE_DATA (Id VARCHAR(20) Primary key, Name VARCHAR(50), Phone Varchar(15), Role Varchar(50),Gender Varchar(15), Salary Decimal(10,2))"
    cursor.execute(table_query)
    cursor.close()
    connection.close()

def insert(id,name,phone,role,gender,salary):
    try:
        connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Aftab@786",
            database="EMPLOYEE_MANAGEMENT_SYSTEM"
        )
        cursor=connection.cursor()
        
    except:
        messagebox.showerror("Error","Mysql Database Error Please Check Manually")
        return
    
    insert_query="INSERT INTO EMPLOYEE_DATA VALUE (%s,%s,%s,%s,%s,%s)"
    data_tuple=(id,name,phone,role,gender,salary)
    cursor.execute(insert_query,data_tuple)
    connection.commit()
    cursor.close()
    connection.close()
    
def fetch_employees():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Aftab@786",
            database="EMPLOYEE_MANAGEMENT_SYSTEM"
        )
        
        cursor = connection.cursor()
        select_query = "SELECT * FROM EMPLOYEE_DATA"
        cursor.execute(select_query)
        result = cursor.fetchall()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Something went wrong: {err}")
        return []
    finally:
        cursor.close()
        connection.close()
    
    return result


def update(id,new_name,new_phone,new_role,new_gender,new_salary):
    try:
        connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Aftab@786",
            database="EMPLOYEE_MANAGEMENT_SYSTEM"
        )
        cursor=connection.cursor()
        
    except:
        messagebox.showerror("Error","Mysql Database Error Please Check Manually")
        return
    
    update_query="UPDATE EMPLOYEE_DATA SET name=%s,phone=%s,role=%s,gender=%s,salary=%s WHERE id=%s"
    data_update=(new_name,new_phone,new_role,new_gender,new_salary,id)
    cursor.execute(update_query,data_update)
    connection.commit()
    cursor.close()
    connection.close()


def delete(id):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Aftab@786",
            database="EMPLOYEE_MANAGEMENT_SYSTEM"
        )
        cursor = connection.cursor()
        
        delete_query = "DELETE FROM EMPLOYEE_DATA WHERE id=%s"
        cursor.execute(delete_query, (id,))
        connection.commit()
        cursor.close()
        connection.close()
        
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"MySQL Database Error: {err}")
        return

def search(option, value):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Aftab@786",
            database="EMPLOYEE_MANAGEMENT_SYSTEM"
        )
        
        cursor = connection.cursor()
        select_query = f"SELECT * FROM EMPLOYEE_DATA WHERE {option}=%s"
        cursor.execute(select_query, (value,))
        result = cursor.fetchall()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Something went wrong: {err}")
        return []
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
    
    return result

def deleteall_records():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Aftab@786",
            database="EMPLOYEE_MANAGEMENT_SYSTEM"
        )
        cursor = connection.cursor()
        
        delete_query = "TRUNCATE TABLE EMPLOYEE_DATA"
        cursor.execute(delete_query)
        connection.commit()
        cursor.close()
        connection.close()
        
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"MySQL Database Error: {err}")
        return
    

create_database()
create_table( )