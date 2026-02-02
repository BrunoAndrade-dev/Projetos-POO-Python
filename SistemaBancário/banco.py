from cliente import Cliente
from conta import Conta 

class ContaNãoEncontrada(Exception) : 
    pass 

class Banco: 
    def __init__ (self, conta_repo, cliente_repo) :
        self.conta_repo = conta_repo 
        self.cliente_repo = cliente_repo
        

    def cadastrar_cliente (self, nome : str , cpf : str) -> Cliente : 
        cliente = Cliente (nome ,cpf)
        self.cliente_repo.salvar_cliente(cliente)
    
        return cliente 
    

    def criar_conta (self, cliente : Cliente, number : int , saldo : float = 0.0) -> Conta : 
        nova_conta = Conta(number , saldo, cliente)
        self.conta_repo.salvar_conta (nova_conta)
        
        return nova_conta
    
    def buscar_conta_por_numero (self, conta_ : int) -> Conta :
        for c in self.contas : 
            if c.number == conta_ :
                return c 
        raise ContaNãoEncontrada("Conta Não Encontrada")
        





        
    
        
