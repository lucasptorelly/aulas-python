orcamento = 500

while orcamento > 0:
    gasto = float(input("Digite o valor do gasto: "))

    orcamento = orcamento - gasto

    print("saldo restante: R$", orcamento)

    print("atenção: você ficou sem ou estourou seu orcamento")