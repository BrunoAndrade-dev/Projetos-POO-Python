class SaldoInsuficienteError(Exception) : 
    pass 

class Conta : 
    def __init__ (self, number, saldo, cliente) : 
        self.number = number 
        self.saldo = saldo 
        self.cliente = cliente

    def sacar(self, valor : float) : 
        if valor <= 0 :
            raise ValueError("Valor inválido")
        
        if self.saldo < valor : 
            raise SaldoInsuficienteError("Saldo Insuficiente")
        
        self.saldo -= valor
        
    def depositar(self, valor) : 
        if valor <= 0 :
            raise ValueError("Valor Inválido")
        self.saldo += valor

    def transferir (self,conta_destino,  valor) : 
        self.sacar(valor)
        conta_destino.depositar(valor)
        self.saldo -= valor 