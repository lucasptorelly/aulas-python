nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
plano = input("Você tem plano de saúde? (Sim ou Não) ")

tem_plano = plano == "Sim"

aceito = idade >= 18 and idade < 60 and tem_plano

print("Seu nome é ", nome, "você tem anos", idade, "tem plano?", tem_plano, "Você foi aceito?", aceito)




