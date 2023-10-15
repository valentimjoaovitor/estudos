'''
6.5. Rios: Atividade python página 147 do livro curso intensivo de python
'''

rios_paises = {'nilo': 'egito',
               'tietê': 'são Paulo',
                'rio prata': 'mato grosso do sul' }

for rio, local in rios_paises.items():
    print(f'{rio.title()} atravessa {local.title()}')

for r in rios_paises:
    print(f'\nNome de rio: ', r)

print(' ')

print('Nome de cada país: ')
for n in rios_paises.values():
    print(n)



