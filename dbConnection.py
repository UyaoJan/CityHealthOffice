import mysql.connector
import os
from dotenv import load_dotenv

env_loc="config.env"
load_dotenv(env_loc)

def get_connection():
    return mysql.connector.connect(
    host=os.getenv('HOST'),
    user=os.getenv('USER'),
    password=os.getenv('PASSWORD'),
    database=os.getenv('DATABASE')
    )

def get_cursor(conn):
    return conn.cursor()