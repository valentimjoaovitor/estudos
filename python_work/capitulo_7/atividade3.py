'''
7.3 múltiplos de dez: atividade da pagina 161
'''

numero = input('Coloque um número e mostrarei se ele é multiplo de 10: ')
numero = int(numero)

mult = numero % 10

if mult == 0:
    print(f'O número {numero} é multiplo de 10')
else:
    print(f'O número {numero} não é multiplo de 10')