numeros = int(input("Digite um numero da tabuada:"))

contador = 1

while contador <= 10:
    resultado = numeros * contador

    print(numeros, "x", contador, "=", resultado)

    contador = contador + 1
