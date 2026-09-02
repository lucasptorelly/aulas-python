nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

frequencia = int(input("Digite a frequencia do aluno: "))

aprovado = media >= 6 and frequencia >= 75

print("O aluno teve media: ", media, "e foi aprovado?", aprovado)