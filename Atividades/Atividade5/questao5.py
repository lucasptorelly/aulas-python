numero1 = int(input("Digite o primeiro número real: "))

numero2 = int(input("Digite o segundo número real: "))

operador = input("Digite a operação +, -, *, /: ")

match operador:
    case "+":
        print(numero1 + numero2)
    case "-":
        print(numero1 - numero2)
    case "*":
        print(numero1 * numero2)
    case "/":
        print(numero1 / numero2)

