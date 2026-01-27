from banco import Banco 
from repository.cliente_repo import clienteRepository
from repository.conta_repo import contaRepository

def criar_banco () -> Banco :

    """
    
    Factory do Banco 

    """
    cliente_repo = clienteRepository()
    conta_repo = contaRepository()

    banco = Banco (
        conta_repo = conta_repo , cliente_repo = cliente_repo
    )
    return banco 

"""

ÚNICA INSTÂNCIA DO BANCO 

"""

banco = criar_banco()
