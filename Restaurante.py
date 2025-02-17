from Menu import Bebida, Prato, Sobremesa, Drink, menu

print('--- Menu de Restaurante ---')

print('')
print('--- Opções ---')
print('')

print('--- 1 - Cadastrar Bebida ')
print('--- 2 - Cadastrar Prato ')
print('--- 3 - Cadastrar Sobremesa ')
print('--- 4 - Cadastrar Drink ')
print('--- 5 - Consultar Menu ')
print('--- 6 - Sair ')

value = 0
_menu = menu()

while( value != 6 ):

    print('')
    value = int(input('Digite a sua opção: '))
    print('')

    match value:
        case 1:
            _bebida = Bebida()
            _bebida.adicionar_nome(input('Digite o Nome:'))
            _bebida.adicionar_valor(input('Digite o Valor: '))
            _bebida.adicionar_descriçao(input('Digite a Descrição: '))

            _menu.adicionar_bebida(_bebida)
        
            print('')
            print('Cadastrado com Sucesso')
            print('')
        
        case 2:
            _prato = Prato()
            _prato.adicionar_nome(input('Digite o Nome: '))
            _prato.adicionar_valor(input('Digite o Valor: '))
            _prato.adicionar_descriçao(input('Digite a Descrição: '))

            _menu.adicionar_prato(_prato)

            print('')
            print('Cadastrado com Sucesso')
            print('')

        case 3:
            _sobremesa = Sobremesa()
            _sobremesa.adicionar_nome(input('Digite o Nome: '))
            _sobremesa.adicionar_valor(input('Digite o Valor: '))
            _sobremesa.adicionar_descriçao(input('Digite a Descrição: '))

            _menu.adicionar_sobremesa(_sobremesa)

            print('')
            print('Cadastrado com Sucesso')
            print('')

        case 4:
            _drink = Drink()
            _drink.adicionar_nome(input('Digite o Nome: '))
            _drink.adicionar_valor(input('Digite o valor: '))
            _drink.adicionar_descriçao(input('Digite a Descrição: '))

            _menu.adicionar_drink(_drink)

            print('')
            print('Cadastrado com Sucesso')
            print('')


        case 5:
            print('Menu')
            print('')

            print('BEBIDAS')
            print('')
            _menu.consultar_bebidas()

            print('DRINKS')
            print('')
            _menu.consultar_drinks()

            print('PRATOS')
            print('')
            _menu.consultar_pratos()

            print('SOBREMESA')
            print('')
            _menu.consultar_sobremesas()

        case 6:
            print('Função de Sair')
            
        case _:
            print('Função desconhecida')

print("Acabou")