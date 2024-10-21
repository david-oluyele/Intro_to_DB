import mysql.connector
from mysql.connector import errorcode

def create_database():
    # Connection parameters
    host = 'localhost'
    user = 'davidoluyele'
    password = '@tycoonTHEdeveloper0607'

    try:
        # Establish a connection to MySQL server
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        cursor = connection.cursor()

        # Create Database
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied for user '{}'. Please check your username and password.".format(user))
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist.")
        else:
            print("Error: {}".format(err))
    finally:
        # Clean up
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()

if __name__ == "__main__":
    create_database()

