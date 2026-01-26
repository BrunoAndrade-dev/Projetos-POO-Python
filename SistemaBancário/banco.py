from cliente import Cliente
from conta import Conta 

class ContaNãoEncontrada(Exception) : 
    pass 

class Banco: 
    def __init__ (self) :
        self.clientes = []
        self.contas = []

    def cadastrarCliente (self, nome : str , cpf : str) -> Cliente : 
        cliente = Cliente (nome ,cpf)
        self.clientes.append()
        return cliente 

    def criarConta (self, cliente : Cliente, number : int , saldo : float = 0.0) -> Conta : 
        nova_conta = Conta(number , saldo, cliente)
        self.contas.append()
        return nova_conta
    
    def buscar_Conta_Por_Numero (self, conta_ : int) -> Conta :
        for c in self.contas : 
            if c.numero == conta_ :
                return c 
        raise ContaNãoEncontrada("Conta Não Encontrada")
        





        
    
        
