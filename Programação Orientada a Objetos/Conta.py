import datetime


class Conta:
    def __init__(self, numero, titular, conta, saldo, limite=1000):
        self.__numero = numero
        self.titular = titular
        self.__conta = conta
        self.__saldo = saldo
        self.__limite = limite

    def Extrato(self):
        print(f"{'-' * 50}\n{' ' * 11}Bem vindo ao Banco Python\n{'-' * 50}\n"
              f"Titular: {self.titular}\nConta: {self.__conta}\nSaldo: R$"
              f"{self.__saldo}\nData do extrato:"
              f"{datetime.datetime.now().strftime('%d')}/"
              f"{datetime.datetime.now().strftime('%m')}/"
              f"{datetime.datetime.now().strftime('%Y')}\nHora "
              f"do "
              f"extrato: "
              f"{datetime.datetime.now().strftime('%I')}:"
              f"{datetime.datetime.now().strftime('%M')}"
              f"{datetime.datetime.now().strftime('%p').lower()}\n")

    def Depositar(self, valor):
        self.__saldo += valor

    def Sacar(self, valor):
        self.__saldo -= valor

    def Transferir(self, valor, destino):
        self.Sacar(valor)
        destino.Depositar(valor)

    def Transferencia(self, valor):
        print(f"{'-' * 50}\n{' ' * 11}Bem vindo ao Banco Python\n{'-' * 50}\n"
              f"Você recebeu uma transferência de {self.titular.upper()}"
              f"\nValor"
              f" recebido: R${valor}\nData da transferência:"
              f"{datetime.datetime.now().strftime('%d')}/"
              f"{datetime.datetime.now().strftime('%m')}/"
              f"{datetime.datetime.now().strftime('%Y')}\nHora "
              f"da transferência: "
              f"{datetime.datetime.now().strftime('%I')}:"
              f"{datetime.datetime.now().strftime('%M')}"
              f"{datetime.datetime.now().strftime('%p').lower()}\n")

    def get_limite(self):
        return self.__limite

    def set_limite(self, newLimite):
        self.__limite = newLimite
        return self.__limite

    def AumentoDeLimite(self, valor):
        print(f"{'-' * 50}\n{' ' * 11}Bem vindo ao Banco Python\n{'-' * 50}\n"
              f"Olá, {self.titular}\nSeu limite do cartão foi de R$"
              f"{self.get_limite()} para R${self.set_limite(valor)}")


nomeTitular = input("Digite o nome completo do titular: ").title()
conta1 = Conta(222, nomeTitular, 212, 10)  # variável nomeia-se "referência"
conta2 = Conta(223, "Manoel Gomes", 213, 1000000)
conta3 = Conta(224, "Thais Carla", 214, 100, 500)

deposito = int(input(f"Olá, {conta1.titular}!\nDigite o valor que deseja "
                     f"depositar: R$"))
conta1.Depositar(deposito)
conta1.Extrato()

valorRecebido = float(input("Digite o valor que deseja transferir: R$"))
conta2.Transferir(valorRecebido, conta1)  # origem.Transferir(<valor>,<destino>)

conta2.Transferencia(valorRecebido)
conta2.Extrato()

conta3.AumentoDeLimite(1500)

outraRef = None  # aponta para nenhuma referência
