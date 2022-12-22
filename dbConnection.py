import mysql.connector

def get_connection():
    return mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="cho_infosy"
    )

def get_cursor(conn):
    return conn.cursor()