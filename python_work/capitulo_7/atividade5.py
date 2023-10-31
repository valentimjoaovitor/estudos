'''
7.5 Ingressos de cinema pagina 168
'''
print('(ENTRADA PARA CINEMA)')
while True:
    print('digite "quit" para sair')
    idade = input('\nColoque sua idade: ')


    if idade.lower() == 'quit':
        break

    if int(idade) < 3:
        print('\ningresso é gratuito')
    
    elif int(idade) >= 3 and int(idade) <= 12:
        print('\nIngresso custa 10R$')

    elif int(idade) > 12:
        print('\nIngresso custa 15R$')


