from .dp import get_connect
from cliente import Cliente
import sqlite3
class SaveError(Exception) : 
    pass

class BuscaError(Exception) : 
    pass

class clienteRepository : 
    def salvar_cliente (self, cliente : Cliente) :
        try : 
            conn = get_connect()
            with conn :
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO clientes (nome, cpf) VALUES (?,?)", (cliente.nome, cliente.cpf)
            )
            conn.close()
        except sqlite3.IntegrityError  : 
            raise Exception ("Erro ao salvar cliente: CPF já existente")
        except sqlite3.Error :
            raise Exception("ERRO NO SQLite ")

    
    def buscar_por_cpf (self, cpf  : str) : 
        try:
            conn = get_connect()
            cursor = conn.cursor()
            cursor.execute("SELECT nome, cpf FROM clientes WHERE cpf = ?", (cpf,))
            row = cursor.fetchone()
            conn.close()

            if row:
                return Cliente(row['nome'], row['cpf'])
            return None
        except sqlite3.Error as e:
            raise BuscaError(f"Erro de busca no banco: {e}")