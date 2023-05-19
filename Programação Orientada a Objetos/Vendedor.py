class Vendedor:
    def __init__(self,nome,vendas = 0):
        self.nome = nome
        self.vendas = vendas
    def Bateumeta(self,meta):
        if self.vendas >= meta:
            print(f"{self.nome.capitalize()} bateu a meta!")
        else:
            print(f"{self.nome} não bateu a meta!")

nomeVendedor = input("Qual o nome do vendedor? ")
totalVendas = float(input("Quanto ele arrecadou nas vendas? R$"))

vendedorInformacoes = Vendedor(nomeVendedor,totalVendas)
vendedorInformacoes.Bateumeta(1000)

