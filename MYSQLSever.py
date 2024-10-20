import mysql.connector
from mysql.connector import Error

def create_database():
    # Connection details
    host = "localhost"
    user = "davidoluyele"
    password = "@tycoonTHEdeveloper0607"
    database_name = "alx_book_store"

    try:
        # Establish a connection to the MySQL server
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )

        if connection.is_connected():
            print("Connected to MySQL Server")

            # Create a cursor to execute SQL statements
            cursor = connection.cursor()

            # Create the database if it doesn't already exist
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
            print(f"Database '{database_name}' created successfully!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()
