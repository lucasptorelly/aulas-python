saldo = 500.00

saque = float(input("Digite o valor que deseja sacar:"))

novo_saldo = saldo - saque

if saque >= saldo:
    print("Saldo insuficiente para realizar esta operação")
else:
    print("Saque realizado com sucesso Saldo atual: R$" , novo_saldo)



