'''
4.12 Mais loops exercício pag 102
'''

my_foods = ['pizza', 'falafel', 'carrot cake' ]
friend_foods = my_foods[:]

print('Minha lista de comida:')
for food in my_foods:
    print(food)

print('\nLista de comidas do amigo:')
friend_foods.append('pão de queijo')
for his_food in friend_foods:
    print(his_food)
