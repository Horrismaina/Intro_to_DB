#!/usr/bin/python3
"""
Script to create the alx_book_store database in MySQL server
"""
import mysql.connector
from mysql.connector import Error

def create_database():
    """Function to create database and handle connection"""
    connection = None
    try:
        # Establish connection to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root"  # Change this to your MySQL password
        )
        
        if connection.is_connected():
            # Create a cursor object to execute queries
            cursor = connection.cursor()
            
            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    
    finally:
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()