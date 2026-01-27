from dp import get_connect
from cliente import Cliente
class SaveError(Exception) : 
    pass

class BuscaError(Exception) : 
    pass

class clienteRepository : 
    def salvar_cliente (self, cliente) :
        try : 
            conn = get_connect()
            cursor = conn.cursor()
        except SaveError as e : 
            print ("Erro ao salvar o cliente ")
    
    def buscar_por_cpf (self, cpf  : str) : 
        raise BuscaError("Erro de busca")