from .dp import get_connect
from conta import Conta
from cliente import Cliente
import sqlite3

class ErrorContaCreate (Exception) : 
    pass

class ErrorFindConta(Exception):
    pass 

class ErrorAtualizarSaldo(Exception) :
    pass 

class contaRepository :
    def salvar_conta (self, conta : Conta) :
        try : 
            conn = get_connect()
            cursor = conn.cursor()
            cursor.execute (
                "INSERT INTO contas (numero, saldo, cpf_cliente) VALUES (?, ?, ?)",
                (conta.number, conta.saldo, conta.cliente.cpf)
            )
            conn.commit()
            conn.close()
        except sqlite3.IntegrityError:
            raise ErrorContaCreate("Número de conta já existente")
        except sqlite3.Error as e:
            raise ErrorContaCreate(f"Erro ao salvar conta: {e}")

    def conta_existe(self, numero : str) -> bool :
        conn = get_connect()
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM contas WHERE numero = ?", (numero,))
        existe = cursor.fetchone() is not None
        conn.close()
        return existe
    
    def buscar_conta (self, number) : 
        try:
            conn = get_connect()
            cursor = conn.cursor()
            cursor.execute(
                """SELECT c.numero, c.saldo, c.cpf_cliente, cl.nome
                   FROM contas c
                   JOIN clientes cl ON c.cpf_cliente = cl.cpf
                   WHERE c.numero = ?""",
                (number,)
            )
            row = cursor.fetchone()
            conn.close()
            if row:
                cliente = Cliente(row['nome'], row['cpf_cliente'])
                return Conta(row['numero'], row['saldo'], cliente)
            return None
        except sqlite3.Error as e:
            raise ErrorFindConta(f"Erro ao buscar conta: {e}")
    
    def atualizar_saldo (self, conta : Conta) : 
        try:
            conn = get_connect()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE contas SET saldo = ? WHERE numero = ?",
                (conta.saldo, conta.number)
            )
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            raise ErrorAtualizarSaldo(f"Erro ao atualizar saldo: {e}")
    
    def busca_conta_por_cpf (self, cpf : str) :
        conn = None
        try:
            conn = get_connect()
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(
                """SELECT c.numero, c.saldo, c.cpf_cliente, cl.nome
                   FROM contas c
                   JOIN clientes cl ON c.cpf_cliente = cl.cpf
                   WHERE cl.cpf = ?""",
                (cpf,)
            )
            row = cursor.fetchone()
            conn.close()
            if row:
                return Conta(row['numero'], row['saldo'], Cliente(row['nome'], row['cpf_cliente']))
            return None
        except sqlite3.Error as e:
            raise ErrorFindConta(f"Erro ao buscar conta por CPF: {e}")
        finally : 
            if conn : 
                conn.close()