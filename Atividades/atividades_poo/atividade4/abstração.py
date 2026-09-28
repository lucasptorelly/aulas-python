from abc import ABC, abstractmethod

class Transporte(ABC):

    def iniciar_processo(self):
        print("Iniciando calculo do frete")

    @abstractmethod
    def calcular_frete(self, distancia):
        pass

class Caminhao(Transporte):

    def calcular_frete(self, distancia):
        return  distancia * 5

class Drone(Transporte):
    def calcular_frete(self, distancia):
        return distancia * 2

caminhao1 = Caminhao()
drone1 = Drone()

transportes = [caminhao1, drone1]

for transporte in transportes:
    print(transporte.calcular_frete(100))
caminhao1.iniciar_processo()

print(caminhao1.calcular_frete(100))

print(drone1.calcular_frete(100))