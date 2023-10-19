'''
6.10 números favoritos: atividade pag 155 curso intensivo de python
'''

numeros_favoritos = {
    'joana': [5, 7, 9],
    'pedro': [7, 9, 5],
    'henrique': [10, 20, 1],
    'angela': [2, 3, 7],
    'joao': [4, 8, 2]
}

for pessoa, numero_favorito in numeros_favoritos.items():
    print(f'\nNome: {pessoa}')
    print(f'Números favoritos: {numero_favorito}')

print('------------(end)------------')