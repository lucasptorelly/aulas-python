numero_secreto = 14
tentativa = 1
palpite = int(input("Digite seu palpite: "))

while palpite != numero_secreto:
    print("numero incorreto")
    tentativa = tentativa + 1

    palpite = int(input("Digite outro palpite: "))

print("Parabens! Você acertou o numero secreto em", tentativa,  "tentativas")

