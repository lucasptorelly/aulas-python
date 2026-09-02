idade = int(input("Digite sua idade: "))
peso = int(input("Digite o seu peso: "))

regras = idade >= 16 and idade <= 69 and peso > 50

print("Pode ser doador?", regras)