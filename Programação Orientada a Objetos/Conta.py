import datetime


class Conta:
    def __init__(self, numero, titular, conta, saldo, limite=1000):
        self.__numero = numero
        self.titular = titular
        self.__conta = conta
        self.__saldo = saldo
        self.__limite = limite
        self.__taxaDeTransferencia = 5.90
        self.__codigoBanco = "020"

    def Extrato(self):
        print(f"{'-' * 50}\n{' ' * 11}Bem vindo ao Banco Python\n{'-' * 50}\n"
              f"Titular: {self.titular}\nConta: {self.__conta}\nSaldo: R$"
              f"{self.__saldo}\nData do extrato:"
              f" {datetime.datetime.now().strftime('%d')}/"
              f"{datetime.datetime.now().strftime('%m')}/"
              f"{datetime.datetime.now().strftime('%Y')}\nHora "
              f"do "
              f"extrato: "
              f"{datetime.datetime.now().strftime('%I')}:"
              f"{datetime.datetime.now().strftime('%M')}"
              f"{datetime.datetime.now().strftime('%p').lower()}\n")

    def Depositar(self, valor):
        self.__saldo += valor

    def __ValorDisponivel(self, valor):
        valorDisponivel = self.__saldo + self.__limite
        return valor <= valorDisponivel

    def Sacar(self, valor):
        if self.__ValorDisponivel(valor):
            self.__saldo -= valor
            print(f"{'-' * 50}\n{' ' * 11}Bem vindo ao Banco Python\n{'-' * 50}\nSeu saque foi "
                  f"concluído!\nValor sacado: R${valor}")
        else:
            print(f"Saldo insuficiente para saque!")

    def __PodeTransferir(self, valor):
        ValorDisponivelTransferencia = (self.__saldo + self.__limite ) - self.__taxaDeTransferencia
        return valor <= ValorDisponivelTransferencia

    def Transferir(self, valor, destino):

        if self.__PodeTransferir(valor):
            self.Sacar(valor)
            destino.Depositar(valor)
            print(f"{'-' * 50}\n{' ' * 11}Bem vindo ao Banco Python\n{'-' * 50}\n"
                  f"Você recebeu uma transferência de {self.titular.upper()}"
                  f"\nValor"
                  f" recebido: R${valor:.2f}\nData da transferência:"
                  f" {datetime.datetime.now().strftime('%d')}/"
                  f"{datetime.datetime.now().strftime('%m')}/"
                  f"{datetime.datetime.now().strftime('%Y')}\nHora "
                  f"da transferência: "
                  f"{datetime.datetime.now().strftime('%I')}:"
                  f"{datetime.datetime.now().strftime('%M')}"
                  f"{datetime.datetime.now().strftime('%p').lower()}\n")
        else:
            print("Saldo insuficiente para transferência!")

    def __set_limite(self, newLimite):
        self.__limite = newLimite
        return self.__limite

    def AumentoDeLimite(self, valor):
        print(f"{'-' * 50}\n{' ' * 11}Bem vindo ao Banco Python\n{'-' * 50}\n"
              f"Olá, {self.titular}\nSeu limite do cartão foi de R$"
              f"{self.__limite} para R${self.__set_limite(valor)}")

    @staticmethod
    def CodigoBanco():
        return "001"


outraRef = None  # aponta para nenhuma referência
