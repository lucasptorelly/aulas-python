class Produto:

    def __init__(self, nome, preco, quantidade_estoque):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade_estoque = quantidade_estoque

    def adicionar_estoque(self, quantidade):
        if quantidade > 0:
            self.__quantidade_estoque = self.__quantidade_estoque + quantidade
        else:
            print("erro: Quantidade inválida")

    def realizar_venda(self, quantidade):
        if quantidade > 0 and quantidade <= self.__quantidade_estoque:
            self.__quantidade_estoque = self.__quantidade_estoque - quantidade

        else:
            print("Venda negada: Estoque insuficiente")
    def aplicar_desconto(self, percentual):
        if percentual > 0 and percentual <= 80:
            desconto = self.__preco * percentual / 100
            self.__preco = self.preco - desconto
        else:
            print("Erro: Desconto inválido")
    def exibir_resumo(self):
        print("Nome:", self.__nome)
        print("Preço: R$", self.__preco)
        print("Quantidade em estoque:", self.__quantidade_estoque)


meu_produto= Produto("Notebook", 3000, 10)
meu_produto.__quantidade_estoque = -50
meu_produto.__preco = -100
meu_produto.realizar_venda(9999)
meu_produto.exibir_resumo()
print(meu_produto.__dict__)


