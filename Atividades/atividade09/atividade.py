class carro:
    def __init__(self, marca, modelo, ano, cor, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = velocidade


    def acelerar(self):
        self.velocidade = self.velocidade + 10

    def frear(self):
        self.velocidade = self.velocidade - 10

    def buzinar(self):
        print("Biii bi")



carro1 = carro("Toyota", "Corolla", 2024, "preto", 0)

carro1.acelerar()
print(carro1.velocidade)
carro1.frear()
print(carro1.velocidade)
carro1.buzinar()
