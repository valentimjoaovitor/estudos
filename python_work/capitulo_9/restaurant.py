class Restaurante:
    def __init__(self, restaurant_name, cuisine_type):
            """Inicializa os atributos de nome e tipo de cozinha"""
            self.nome = restaurant_name
            self.cozinha = cuisine_type

    def describe_restaurant(self):
            print(f"restaurant's name : {self.nome}")
            print(f"The cuisine type is: {self.cozinha}")

    def open_restaurant(self):
            print('\nThe restaurant is open...')
