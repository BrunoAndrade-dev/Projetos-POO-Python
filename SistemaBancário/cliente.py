class Cliente : 
    def __init__ (self, nome : str, cpf: str) : 
        self.nome = nome 
        self.cpf = cpf
        self._contas = []
    
    @property

    def contas(self) : 
        return self.contas.copy()

    def adicionar_conta (self, conta ) : 
        self._contas.append(conta)
    
    

