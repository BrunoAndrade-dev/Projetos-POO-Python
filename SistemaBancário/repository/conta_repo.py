from dp import get_connect
from conta import Conta
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
                "INSERT INTO contas (numero, saldo, cpf_cliente)" , (conta.number, conta.saldo, conta.cliente.cpf)
            )
            conn.commit()
            conn.close()
        except ErrorContaCreate as e : 
            print ("Erro ao salvar conta")
    
    def buscar_conta (self, number) : 
        raise ErrorFindConta("Erro ao encontrar conta")
    
    def atualizar_saldo (self, conta) : 
        raise ErrorAtualizarSaldo("Erro ao atualizar Saldo")