class Pessoa:
    def __init__(self, nome, idade, peso, comer=False, falar=False, dormir=False
                 ):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.comer = comer
        self.falar = falar
        self.dormir = dormir

    def Comer(self, ali):
        if self.falar and not self.comer:
            print(f"{self.nome} não pode comer pois já está falando")
            self.falar = False
        elif not self.comer:
            print(f"{self.nome} começou a comer {ali}")
            self.comer = True
        else:
            print(f"{self.nome} já está comendo")

    def PararDeComer(self):
        if self.comer:
            print(f"{self.nome} parou de comer")
            self.comer = False
        else:
            print(f"{self.nome} não estava comendo")

    def Falar(self):
        if not self.falar and not self.comer:
            print(f"{self.nome} está falando")
            self.falar = True
        elif self.falar:
            print(f"{self.nome} já está falando")

    def PararDeFalar(self):
        if self.falar:
            print(f"{self.nome} parou de falar")
            self.falar = False
        else:
            print(f"{self.nome} não estava falando")

    def Dormir(self):
        if not self.dormir and self.falar or self.comer:
            print(f"{self.nome} não pode dormir agora")
            self.falar = False
            self.comer = False
        elif not self.dormir:
            print(f"{self.nome} está indo dormir")
            self.dormir = True
        else:
            print(f"{self.nome} já está dormindo")


pessoa = Pessoa("Tiago", 20, 58)
pessoa.Comer("lasanha")
pessoa.Dormir()
pessoa.PararDeComer()
pessoa.Comer("feijão")
pessoa.PararDeFalar()
pessoa.PararDeComer()
pessoa.PararDeFalar()
pessoa.Comer("hamburguer")
pessoa.PararDeComer()
pessoa.Falar()
pessoa.PararDeFalar()
pessoa.PararDeFalar()
pessoa.Dormir()
pessoa.Dormir()
