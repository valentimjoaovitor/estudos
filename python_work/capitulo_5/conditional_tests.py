'''
5.2 mais testes condicionais oag 116
'''

bolo = 'saudável'
print('O bolo é saudável?')
print(bolo == 'saudável')

print('\nO bolo não é saudável?')
print(bolo == 'não é saudável')

# -----------------------------------------

comida = 'GOSTOSA'
print('\nA comida está gostosa?')
print(comida.lower() == 'gostosa')

print('\nA comida não está gostosa?')
print(comida.lower() == 'ruim')

# ------------------------------------------

valor1 = 20
print('\nSerá que valor é menor que 10?')
print(valor1 <= 10)

print('\nSera que valor é igual a 20?')
print(valor1 == 20)

print('\nvalor é diferente a 20?')
print(valor1 != 20)

print('\nvalor é maior ou igual a 15')
print(valor1 >= 15)

# -------------------------------------------
print('\n "or" and "and"')
valor2 = 40
if valor2 >= 10 and valor2 <= 41:
    print('\n', valor2)

valor3 = 20
if valor3 == 15 or valor3 <= 30:
    print('\n',valor3)

# --------------------------------------------
print(' ')
print('verificando se um valor está na lista "numero"')
numero = [1,2,3,4,5,6,7,8,9,10,11,13]

print(12 in numero)

# --------------------------------------------

if 12 not in numero:
    print('\nO número 12 não está na lista')
else:
    print('\nO número 12 está na lista')