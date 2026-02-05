from cliente import Cliente
from conta import Conta 

class ContaNãoEncontrada(Exception) : 
    pass 

class Banco: 
    def __init__ (self, conta_repo, cliente_repo) :
        self.conta_repo = conta_repo 
        self.cliente_repo = cliente_repo
        

    def cadastrar_cliente (self, nome : str , cpf : str) -> Cliente : 
        if self.cliente_repo.cpf_existe(cpf) :
            raise ValueError(f" O CPF {cpf} ja foi cadastrado no sistema do banco")
        cliente = Cliente (nome ,cpf)
        self.cliente_repo.salvar_cliente(cliente)
        return cliente 
    

    def criar_conta (self, cliente : Cliente, number : int , saldo : float = 0.0) -> Conta : 
        if self.cotna_repo.conta_existe(number) :
            raise ValueError (f"O número da conta {number} ja foi cadastrado no sistema do banco")    
        nova_conta = Conta(number , saldo, cliente)
        self.conta_repo.salvar_conta (nova_conta)
        
        return nova_conta
    
    def buscar_conta_por_numero (self, conta_ : int) -> Conta :
        conta = self.conta_repo.buscar_conta(conta_)
        if conta is None:
            raise ContaNãoEncontrada("Conta Não Encontrada")
        return conta
        





        
    
        
