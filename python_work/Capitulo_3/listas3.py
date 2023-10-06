'''
3.3 Sua própria lista: Pense em seu meio de transporte favorito, como uma moto ou um carro,
e crie uma lista que armazene diversos exemplos. Use sua lista para exibir uma série de declarações
sobre esses itens, como "Gostaria de ter uma moto da Honda".
'''
transporte_fav = ['Carro', 'Bicicleta', 'Skate', 'Pé', 'moto']
message = 'Gostaria de andar de: '

i = int(input('Coloque um número para ver com qual maneira de transporte você vai andar: ')) -1


print(message + transporte_fav[i])

