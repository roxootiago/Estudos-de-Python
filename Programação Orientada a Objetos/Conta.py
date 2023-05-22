import datetime


class Conta:
    def __init__(self, numero, titular, conta, saldo, limite=1000):
        self.__numero = numero
        self.titular = titular
        self.__conta = conta
        self.__saldo = saldo
        self.__limite = limite

    def Extrato(self):
        print(f"{'-'*50}\n{' '*11}Bem vindo ao Banco Python\n{'-'*50}\n"
              f"Titular: {self.titular}\nConta: {self.__conta}\nSaldo: R${self.__saldo}\nData do extrato: "
              f"{datetime.datetime.now().strftime('%x')}\nHora do extrato: {datetime.datetime.now().strftime('%I')}:"
              f"{datetime.datetime.now().strftime('%M')}{datetime.datetime.now().strftime('%p').lower()}")

    def Depositar(self, valor):
        self.__saldo += valor

    def Sacar(self, valor):
        self.__saldo -= valor

    def Transferir(self,valor,destino):
        self.Sacar(valor)
        destino.Depositar(valor)


nomeTitular = input("Digite o nome completo do titular: ").title()
conta1 = Conta(222, nomeTitular, 212, 10)  # variável nomeia-se "referência"
conta2 = Conta(223, "Manoel Gomes", 213, 1000000)
conta3 = Conta(224, "Thais Carla", 214, 100, 500)

deposito = int(input(f"Olá, {conta1.titular}!\nDigite o valor que deseja depositar: R$"))
conta1.Depositar(deposito)
conta1.Extrato()

conta1._Conta__saldo = 50#evitar fazer isso
conta1.Extrato()
conta2.Transferir(2000,conta1)#origem.Transferir(<valor>,<destino>)
conta1.Extrato()

outraRef = None  # aponta para nenhuma referência
