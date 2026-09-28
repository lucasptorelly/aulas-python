class Animal:
    def __init__(self, nome, idade, nivel_fome):
        self.__nome = nome
        self.__idade = idade
        self.__nivel_fome = nivel_fome


    @property
    def nome(self):
        return self.__nome
    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, nova_idade):
        if nova_idade >= 0:
            self.__idade = nova_idade
        else:
            print("Erro: Idade inválida")

    @property
    def nivel_fome(self):
        return self.__nivel_fome


    @nivel_fome.setter
    def nivel_fome(self, novo_nivel):
        if  novo_nivel <0:
            self.__nivel_fome = 0
        elif novo_nivel > 100:
            self.__nivel_fome = 100
        else:
            self.__nivel_fome = novo_nivel
            print("Erro: nível de fome inválido")

animal1 = Animal("Rex", 5, 7)
print(animal1.nome)
print(animal1.idade)
print(animal1.nivel_fome)
