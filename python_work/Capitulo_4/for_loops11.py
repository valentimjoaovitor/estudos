'''
4.11 Minhas pizzas, suas pizzas pag 102
'''

tipos_pizza = ['pepperoni', 'portuguesa', 'frango']
friend_pizza = tipos_pizza[:]

tipos_pizza.append('doce')
friend_pizza.append('nutella')

print('Minhas pizzas favoritas são: ')
for pizzas in tipos_pizza:
    print(pizzas)

print('\nMinhas pizzas favoritas são: ')
for pizzas_do_amigos in friend_pizza:
    print(pizzas_do_amigos)
