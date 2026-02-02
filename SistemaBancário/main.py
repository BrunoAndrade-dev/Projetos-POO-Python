from banco import Banco 
from repository.cliente_repo import clienteRepository
from repository.conta_repo import contaRepository
from repository.dp import criar_tabelas

def criar_banco () -> Banco :

    """
    
    Factory do Banco 

    """
    criar_tabelas()

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
