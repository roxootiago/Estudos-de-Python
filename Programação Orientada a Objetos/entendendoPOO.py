class Computador:
    #Estado do computador(características)
    def __init__(self,marca,memoriaRam,placaDeVideo):
        self.marca = marca
        self.memoriaRam = memoriaRam
        self.placaDeVideo = placaDeVideo

    #Comportamento do computador(funcionalidades)
    def ligar(self):
        print("Ligando...")
    def desligar(self):
        print("Desligando...")
    def estadoComputador(self):
        print(
            f"Marca: {self.marca.capitalize()}\nMemoria ram:"
            f" {self.memoriaRam}Gb\nPlaca de vídeo:"
            f" {self.placaDeVideo.capitalize()}")

peca1 = input("Digite a marca do seu computador: ")
peca2 = input("Digite a memoria ram do seu computador: ")
peca3 = input("Digite a placa de vídeo do seu computador: ")

computador1 = Computador(peca1,peca2,peca3)
computador1.ligar()
computador1.desligar()
computador1.estadoComputador()
