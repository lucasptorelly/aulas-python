opcao = int(input("Digite 1 para saudação ou 2 para sair"))

while opcao != 2:
    if opcao == 1:
        print("Olá, seja bem vindo!")
    else:
        print("Senha incorreta")
    opcao = int(input("Digite 1 para saudação ou 2 para sair"))

print("Programa encerrado")
