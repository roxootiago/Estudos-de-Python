class conta:
    def __init__(self, numero, titular, conta, saldo, limite=1000):
        self.numero = numero
        self.titular = titular
        self.conta = conta
        self.saldo = saldo
        self.limite = limite

    def Extrato(self):
        print(f"Titular: {self.titular}\nConta: {self.conta}\nSaldo: R${self.saldo}")

    def Depositar(self, valor):
        self.saldo += valor

    def Sacar(self,valor):
        self.saldo -= valor

conta1 = conta(222, "Tiago", 212, 10)  # variável nomeia-se "referência"
conta2 = conta(223, "Manoel Gomes", 213, 1000000)
conta3 = conta(224, "Thais Carla", 214, 100, 500)

deposito = int(input("Digite o valor que deseja depositar: R$"))

conta1.Extrato()
conta1.Sacar(deposito)
conta1.Extrato()

