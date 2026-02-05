from .dp import get_connect
from cliente import Cliente
import sqlite3
class SaveError(Exception) : 
    pass

class BuscaError(Exception) : 
    pass

class clienteRepository : 
    def salvar_cliente (self, cliente : Cliente) :
        conn = None
        try : 
            conn = get_connect()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO clientes (nome, cpf) VALUES (?,?)", (cliente.nome, cliente.cpf)
            )
            conn.commit()
        except sqlite3.IntegrityError  : 
            if conn:
                conn.rollback()
            raise Exception ("Erro ao salvar cliente: CPF já existente")
        except sqlite3.Error as e:
            if conn:
                conn.rollback()
            raise Exception(f"Erro no SQLite: {e}")
        finally:
            if conn:
                conn.close()

    def cpf_existe (self, cpf : str) -> bool : 
        conn = get_connect()
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM clientes WHERE cpf = ?" , (cpf,))
        existe = cursor.fetchone() is not None
        conn.close()
        return existe

    
    def buscar_por_cpf (self, cpf  : str) : 
        conn = None
        try:
            conn = get_connect()
            cursor = conn.cursor()
            cursor.execute("SELECT nome, cpf FROM clientes WHERE cpf = ?", (cpf,))
            row = cursor.fetchone()
            if row:
                return Cliente(row['nome'], row['cpf'])
            return None
        except sqlite3.Error as e:
            raise BuscaError(f"Erro de busca no banco: {e}")
        finally:
            if conn:
                conn.close()
    
    def busca_todos_clientes (self) : 
        conn = get_connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clientes")
        rows = cursor.fetchall()
        conn.close()
        return [Cliente(nome = row['nome'], cpf = row['cpf']) for row in rows]