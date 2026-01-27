class ErrorContaCreate (Exception) : 
    pass

class ErrorFindConta(Exception):
    pass 

class ErrorAtualizarSaldo(Exception) :
    pass 

class contaRepository :
    def salvar_conta (self, conta) : 
        raise ErrorContaCreate("ERRO AO SLAVAR CONTA")
    
    def buscar_conta (self, number) : 
        raise ErrorFindConta("Erro ao encontrar conta")
    
    def atualizar_saldo (self, conta) : 
        raise ErrorAtualizarSaldo("Erro ao atualizar Saldo")