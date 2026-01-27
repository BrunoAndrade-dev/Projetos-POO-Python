import sqlite3 
from sqlite3 import Connection

def get_connect () -> Connection : 
    conn = sqlite3.connect('banco_de_dados.db')
    conn.row_factory = sqlite3.Row
    return conn 