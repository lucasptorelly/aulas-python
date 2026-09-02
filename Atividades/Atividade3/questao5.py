valor_compra = int(input("Digite o valor da compra: "))
vip = int(input("Você é vip? Digite 1 para sim ou 0 para não "))


frete_gratis = valor_compra > 200 or vip == 1

print("Tem direito a frete gratis", frete_gratis)

