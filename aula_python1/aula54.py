lista = []

import os

while True:
    print('\n\t-Selecione uma Opção-')
    escolha = input('[I]nserir | [A]pagar | [L]istar: ')

    if len(escolha) > 1:        # se a pessoa colocar uma respota maior que necessário.
        print('escolha inválida')
        continue
    
    if escolha.lower() == 'i':  # Se a pessoa quiser inserir.
        os.system('cls')
        produto = input('Insira o valor aqui: ')
        lista.append(produto)
    
    elif escolha.lower() == 'a':   # Se a pessoa quiser apagar.

        os.system('cls')
        for numero, products in enumerate(lista):
            print(numero ,products)   

        i = int(input('Coloque o índice do produto para remover: '))

        if lista == []:
            print('Não tem produtos na lista') 
            
        elif i <= len(lista):
            try:
                del lista[i]
            except IndexError:
                valor = i - 1
                del lista[valor]   


        else:
            print('Indíce inválido')
    
    elif escolha.lower() == 'l':    # Se a pessoa escolher L de listar

        if lista == []:   # verificar se tem um valor na lista antes de mostrar ela         
            os.system('cls')        # se não tiver nada na lista, irá mostrar que ela está vazia.
            print('Sua lista está vazia...')

        else:       # se tiver algo na lista irá mostrar ela.

            for indice, p in enumerate(lista):
                print('---------------------------')
                print(f'{indice} {p}')
    
    else:
        os.system('cls')
        print('resposta inválida')

# # Solução do professor
# """
# Faça uma lista de comprar com listas
# O usuário deve ter a possibilidade de
# inserir, apagar e listar valores da sua lista
# Não permita que o programa quebre com 
# erros de índices inexistentes na lista.
# """
# import os

# lista = []

# while True:
#     print('Selecione uma opção')
#     opcao = input('[i]nserir [a]pagar [l]istar: ')

#     if opcao == 'i':
#         os.system('clear')
#         valor = input('Valor: ')
#         lista.append(valor)
#     elif opcao == 'a':
#         indice_str = input(
#             'Escolha o índice para apagar: '
#         )

#         try:
#             indice = int(indice_str)
#             del lista[indice]
#         except ValueError:
#             print('Por favor digite número int.')
#         except IndexError:
#             print('Índice não existe na lista')
#         except Exception:
#             print('Erro desconhecido')
#     elif opcao == 'l':
#         os.system('clear')

#         if len(lista) == 0:
#             print('Nada para listar')

#         for i, valor in enumerate(lista):
#             print(i, valor)
#     else:
#         print('Por favor, escolha i, a ou l.')