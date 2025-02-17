from menu import restaurante, menu

print('--- Menu de Restaurante ---')

print('')
print('--- Opções ---')
print('')

print('--- 1 - Cadastrar Produto ')
print('--- 2 - Consultar Menu ')
print('--- 3 - Sair ')

value = 0
lista_de_produtos = restaurante()

while( value != 3 ):

    print('')
    value = int(input('Digite a sua opção: '))
    print('')

    match value:
        case 1:
            _restaurante = restaurante()
            _restaurante.adicionar_nome(input('Digite o Nome:'))
            _restaurante.adicionar_valor(input('Digite o Valor: '))
            _restaurante.adicionar_descriçao(input('Digite a Descrição: '))
        
            print('')
            print('Cadastrado com Sucesso')
            print('')

        case 2:
            print('Lista de produtos')
            print('')

        case 3:
            print('Função de Sair')
        case _:
            print('Função desconhecida')

print("Acabou")