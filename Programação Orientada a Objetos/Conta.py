import datetime

class conta:
    def __init__(self, numero, titular, conta, saldo, limite=1000):
        self.numero = numero
        self.titular = titular
        self.conta = conta
        self.saldo = saldo
        self.limite = limite

    def Extrato(self):
        print(f"Titular: {self.titular}\nConta: {self.conta}\nSaldo: R${self.saldo}\nData do extrato: "
              f"{datetime.datetime.now().strftime('%x')}\nHora do extrato: {datetime.datetime.now().strftime('%I')}:"
              f"{datetime.datetime.now().strftime('%M')}{datetime.datetime.now().strftime('%p').lower()}")

    def Depositar(self, valor):
        self.saldo += valor

    def Sacar(self, valor):
        self.saldo -= valor


nomeTitular = input("Digite o nome completo do titular: ").title()
conta1 = conta(222, nomeTitular, 212, 10)  # variável nomeia-se "referência"
conta2 = conta(223, "Manoel Gomes", 213, 1000000)
conta3 = conta(224, "Thais Carla", 214, 100, 500)

deposito = int(input(f"Olá, {conta1.titular}!\nDigite o valor que deseja depositar: R$"))
conta1.Depositar(deposito)
conta1.Extrato()
outraRef = None#aponta para nenhuma referência
