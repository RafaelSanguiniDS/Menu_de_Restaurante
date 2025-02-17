class restaurante:
    def __init__(self):
        self.nome = ''
        self.valor = ''
        self.descriçao= ''


    def adicionar_nome(self, nome):
        self.nome = nome
        
    def adicionar_valor(self, valor):
        self.valor = valor

    def adicionar_descriçao(self, descriçao):
        self.descriçao = descriçao

    def escrever_nome(self):
        print(f'nome: {self.nome}')
        
    def escrever_valor(self):
        print(f'valor: {self.valor}')

    def escrever_descriçao(self):
        print(f'descriçao: {self.descriçao}')

class menu:
    def __init__(self):
        self.adicionar_produto = []

    def adicionar_produto(self, restaurante):
        self.adicionar_produto.append(restaurante)

    def consultar_carro(self):
        for restaurante in self.adicionar_produto:
            restaurante.escrever_nome()
            restaurante.escrever_valor()
            restaurante.escrever_descriçao()
            print('')