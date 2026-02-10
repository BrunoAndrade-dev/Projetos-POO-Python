from cliente import Cliente
from conta import Conta
from repository.conta_repo import contaRepository

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
    

    def criar_conta (self, cpf_ou_cliente, number : int , saldo : float = 0.0) -> Conta : 
        if self.conta_repo.conta_existe(number) :
            raise ValueError (f"O número da conta {number} ja foi cadastrado no sistema do banco")    
        if isinstance(cpf_ou_cliente, str) : 
            cliente_obj = self.cliente_repo.buscar_por_cpf(cpf_ou_cliente)
        else : 
            cliente_obj = cpf_ou_cliente
        nova_conta = Conta(number , saldo, cliente_obj)
        self.conta_repo.salvar_conta (nova_conta)
        
        return nova_conta
    
    def buscar_conta_por_numero (self, conta_ : int) -> Conta :
        conta = self.conta_repo.buscar_conta(conta_)
        if conta is None:
            raise ContaNãoEncontrada("Conta Não Encontrada")
        return conta
    
    def saldo (self, numero_conta ) :
        conta = self.buscar_conta_por_numero(numero_conta)
        return conta.saldo
        





        
    
        
