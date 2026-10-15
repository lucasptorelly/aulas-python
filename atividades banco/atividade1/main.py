import json

# Lista de arquivos JSON
arquivos = ["base1.json", "base2.json", "base3.json"]

# Lista para armazenar todos os dados
dados_gerais = []

# Ler os três arquivos
for nome_arquivo in arquivos:
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

        if isinstance(dados, list):
            dados_gerais.extend(dados)
        else:
            dados_gerais.append(dados)

# Mostrar os registros
print("===== DADOS CONSOLIDADOS =====")

for registro in dados_gerais:
    print(registro)

# Quantidade total de registros
print("\n===== RESUMO =====")
print(f"Total de registros: {len(dados_gerais)}")

# Salvar todos os dados em um único JSON
with open("base_consolidada.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados_gerais, arquivo, ensure_ascii=False, indent=4)

print("\nArquivo consolidado criado com sucesso!")