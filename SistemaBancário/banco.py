from cliente import Cliente
from conta import Conta 

class ContaNãoEncontrada(Exception) : 
    pass 

class Banco: 
    def __init__ (self, conta_repo, cliente_repo) :
        self.clientes = []
        self.contas = []
        self.contaRepository = conta_repo 
        self.clienteRepository = cliente_repo

    def cadastrar_cliente (self, nome : str , cpf : str) -> Cliente : 
        cliente = Cliente (nome ,cpf)
        self.clienteRepository.salvar_cliente(cliente)
        self.clientes.append(cliente)
        return cliente 
    

    def criar_conta (self, cliente : Cliente, number : int , saldo : float = 0.0) -> Conta : 
        nova_conta = Conta(number , saldo, cliente)
        self.contas.append(nova_conta)
        return nova_conta
    
    def buscar_conta_por_numero (self, conta_ : int) -> Conta :
        for c in self.contas : 
            if c.number == conta_ :
                return c 
        raise ContaNãoEncontrada("Conta Não Encontrada")
        





        
    
        
