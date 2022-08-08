class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Contruindo objetos ... {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        
    def extrato(self):
        print("Saldo {} do titular {}".format(self.saldo, self.titular))
    
    def deposita(self, valor):
        self.saldo += valor
    
    def saca(self, valor):
        self.saldo -= valor
    
