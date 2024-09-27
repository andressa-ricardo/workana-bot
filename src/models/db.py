import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def conectar_banco():
    conn = mysql.connector.connect(
        host=os.getenv('HOST'),
        user=os.getenv('USER'),
        password=os.getenv('PASSWORD'),
        database=os.getenv('DATABASE')
    )
    return conn
