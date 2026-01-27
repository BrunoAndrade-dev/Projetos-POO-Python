from dp import get_connect
from cliente import Cliente
class SaveError(Exception) : 
    pass

class BuscaError(Exception) : 
    pass

class clienteRepository : 
    def salvar_cliente (self, cliente : Cliente) :
        try : 
            conn = get_connect()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO clientes (nome, cpf) VALUES (?,?)", (cliente.nome, cliente.cpf)
            )

            conn.commit()
            conn.close()
        except SaveError as e : 
            print ("Erro ao salvar o cliente ")
    
    def buscar_por_cpf (self, cpf  : str) : 
        raise BuscaError("Erro de busca")