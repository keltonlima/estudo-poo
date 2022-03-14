class Conta():
    
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto...")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        
    def extrato(self):
        print("Número da conta: ", self.__numero,"\nTitular: ", 
              self.__titular,"\nSaldo: ", self.__saldo,
              "\nLimite da conta:", self.__limite)
        
    def deposita(self, valor):
        self.__saldo += valor
    
    def __permite_sacar(self, valor_a_sacar):
        valor_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar
    
    def saca(self, valor):
        if self.__permite_sacar(valor):
            self.__saldo -= valor
        else:
            print("Valor insuficiente!")
        
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
    
    @property    
    def titular(self):
        return self.__titular
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, valor):
        self.__limite = valor
        
    @staticmethod
    def codigo_banco():
        return "001"

if __name__ == "__main__":
    Conta()