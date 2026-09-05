

escolha = int(input("Digite uma opção de 1 a 4: "))

match escolha:
    case 1:
        print("Você escolheu cachorro-quente que custa R$ 10,00")
    case 2:
        print("Você escolheu Hambúrguer que custa R$ 15,00")
    case 3:
        print("Você escolheu Batata frita que custa R$ 8,00")
    case 4:
        print("Você escolheu Refrigerante que custa R$ 5,00")
    case _:
        print("Escolha inválida")
