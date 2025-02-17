class menu:
    def __init__(self):
        self.bebidas = []
        self.pratos = []
        self.drinks = []
        self.sobremesa = []


    def adicionar_bebida(self, bebida):
        self.bebidas.append(bebida)
    
    def adicionar_prato(self, prato):
        self.pratos.append(prato)
    
    def adicionar_sobremesa(self, sobremesa):
        self.sobremesa.append(sobremesa)
    
    def adicionar_drink(self, drink):
        self.drinks.append(drink)

    def consultar_bebidas(self):
        for bebida in self.bebidas:
            bebida.escrever_nome()
            bebida.escrever_valor()
            bebida.escrever_descriçao()
            print('')
    
    def consultar_pratos(self):
        for prato in self.pratos:
            prato.escrever_nome()
            prato.escrever_valor()
            prato.escrever_descriçao()
            print('')

    def consultar_drinks(self):
        for drink in self.drinks:
            drink.escrever_nome()
            drink.escrever_valor()
            drink.escrever_descriçao()
            print('')

    def consultar_sobremesas(self):
        for sobremesa in self.sobremesa:
            sobremesa.escrever_nome()
            sobremesa.escrever_valor()
            sobremesa.escrever_descriçao()
            print('')





class Bebida:
    def __init__(self):
        self.nome = ''
        self.valor = ''
        self.descriçao = ''

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

class Prato:
    def __init__(self):
        self.nome = ''
        self.valor = ''
        self.descriçao = ''

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

class Drink:
    def __init__(self):
        self.nome = ''
        self.valor = ''
        self.descriçao = ''

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

class Sobremesa:
    def __init__(self):
        self.nome = ''
        self.valor = ''
        self.descriçao = ''

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