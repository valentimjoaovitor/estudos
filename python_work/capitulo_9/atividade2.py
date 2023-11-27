'''
9.2 Três Restaurantes: atividade da página 211
'''

class Restaurant:
    
    def __init__(self, restaurant_name, cuisine_type):
        """Inicializa os atributos de nome e tipo de cozinha"""
        self.nome = restaurant_name
        self.cozinha = cuisine_type

    def describe_restaurant(self):
        print(f"restaurant's name : {self.nome}")
        print(f"The cuisine type is: {self.cozinha}")

    def open_restaurant(self):
        print('\nThe restaurant is open...')


restaurante1 = Restaurant('veganinhos', 'vegana')
restaurante2 = Restaurant('carnivorinhos', 'churrasco')
restaurante3 = Restaurant('exotóticos', 'exótica')

restaurante1.describe_restaurant()
restaurante2.describe_restaurant()
restaurante3.describe_restaurant()