nome_produto = input("Digite o nome do produto: ")
custo = float(input("Digite o custo do produto: "))
venda = float(input("Digite o valor da venda do produto: "))

lucro = venda - custo

lucro2 = lucro > 20

print(nome_produto , lucro , lucro2)