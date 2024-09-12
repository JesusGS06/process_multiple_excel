import os
import mysql.connector
from mysql.connector import Error

def insert_rooms_and_employees_in_bulk(df):
    connection = None
    cursor = None

    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )

        if connection.is_connected():
            cursor = connection.cursor()

            insert_query_rooms = f"""
            INSERT INTO rooms (type, price, status) VALUES (%s, %s, %s)
            """
            rooms_data = df[['type', 'price', 'status']].dropna().to_records(index=False).tolist()
            cursor.executemany(insert_query_rooms, rooms_data)
            connection.commit()
            print(f"{cursor.rowcount} rows inserted successfully.")

            insert_query_employees = f"""
            INSERT INTO employees (name, occupation, salary, date_of_entry) VALUES (%s, %s, %s, %s)
            """
            employees_data = df[['name', 'occupation', 'salary', 'date_of_entry']].dropna().to_records(index=False).tolist()
            cursor.executemany(insert_query_employees, employees_data)
            connection.commit() 
            print(f"{cursor.rowcount} rows inserted successfully.")   

    except Error as e:
        print(f"Error: {e}")
        if connection:
            connection.rollback()

    finally:
        if cursor is not None: 
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()
