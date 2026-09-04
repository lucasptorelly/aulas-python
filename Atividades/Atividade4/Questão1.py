valor = int(input("Digite um número inteiro:"))

par_impar = valor % 2

if par_impar == 0:
    print("O número", valor , "é Par")
else:
    print("O número", valor, "é impar")