class conta:
    def __init__(self,numero,titular,conta,saldo,limite = 1000):
        self.numero = numero
        self.titular = titular
        self.conta = conta
        self.saldo = saldo
        self.limite = limite



conta1 = conta(222,"Tiago",212,90000)#variável nomeia-se "referência"
conta2 = conta(223,"Manoel Gomes",213,1000000)
conta3 = conta(224,"Thais Carla",214,100,500)

print(f"Saldo: R${conta2.saldo}")