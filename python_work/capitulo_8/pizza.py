# def make_pizza(*toppings):
#     """Sintetiza a pizza que estamos prestes a fazer"""
#     print('\nMaking a pizza with the following toppings:')
#     for topping in toppings:
#         print(f"- {topping}")

# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

# Misturando argumentos posicionais e arbitrários
def make_pizza(size, *toppings):
    """ Sintetiza a pizza que estamos prestes a fazer"""
    print(f"\nMaking a {size} -inch pizza with the following toppings: ")
    for topping in toppings:
        print(f'- {topping}')
