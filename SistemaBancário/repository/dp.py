import sqlite3
from sqlite3 import Connection
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "banco_de_dados.db")

def get_connect() -> Connection:
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def criar_tabelas():
    conn = get_connect()
    cursor = conn.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS clientes(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nome TEXT NOT NULL,
                       cpf TEXT NOT NULL UNIQUE
                   )
                   """)
    cursor.execute("""
                  CREATE TABLE IF NOT EXISTS contas(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            numero INTEGER NOT NULL UNIQUE,
            saldo REAL NOT NULL,
            cpf_cliente TEXT NOT NULL,
            FOREIGN KEY (cpf_cliente) REFERENCES clientes(cpf)
        )""")
    conn.commit()
    conn.close() 

