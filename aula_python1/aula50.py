"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""

lista = ['maria', 'helena', 'luiz']
lista.append('pedrinho')

i = 0
for nome in lista:

    print(f'{i} {nome}')
    i += 1


# teacher's solution

# lista = ['Maria', 'Helena', 'Luiz']
# lista.append('João')


# indices = range(len(lista))

# for indice in indices:
#     print(indice, lista[indice], type(lista[indice]))