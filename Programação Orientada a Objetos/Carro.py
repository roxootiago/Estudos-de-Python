class carro:
    def __init__(self,cor,ano,modelo):
        self.cor = cor
        self.ano = ano
        self.modelo  = modelo

    def ligar(self):
        print(f"Ligando o {self.modelo.capitalize()}")

    def acelerar(self):
        print(f"Acelerando  o {self.modelo.capitalize()}")

    def informacoes(self):
        print(f"Modelo: {self.modelo.capitalize()}\nAno: {self.ano}\nCor:"
        f"{self.cor.capitalize()}")

corCarro = input("Qual a cor do carro? ")
anoCarro = int(input("Qual o ano do carro? "))
modeloCarro = input("Qual o modelo do carro? ")

carroInformacoes = carro(corCarro,anoCarro,modeloCarro)
carroInformacoes.ligar()
carroInformacoes.acelerar()
carroInformacoes.informacoes()