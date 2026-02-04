from banco import Banco 
from repository.cliente_repo import clienteRepository
from repository.conta_repo import contaRepository
from repository.dp import criar_tabelas, DB_PATH

def criar_banco () -> Banco :

    """
    
    Factory do Banco 

    """
    criar_tabelas()
    # Garante que o app usa sempre este arquivo (evita confusão com outro .db na raiz do projeto)
    print(f"[Sistema Bancário] Banco de dados em: {DB_PATH}")

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
