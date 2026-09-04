idade = int(input("Digite sua idade: "))

vip = int(input("Possui convite vip? Digite 1 para sim ou 0 para não: "))

organizador = int(input("É organizador do evento? Digite 1 para sim ou 0 para não: "))



if (idade >= 18 and vip == 1) or organizador == 1:
    print("Entrada permitida!")
else:
    print("Entrada negada")