"""
Atividade 9.4 Pessoas atendidas, página 216
"""

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type, number_served = 0):
        """Inicializa os atributos de nome e tipo de cozinha"""
        self.nome = restaurant_name
        self.cozinha = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        """Apresenta informações sobre o restaurante."""
        print(f"restaurant's name : {self.nome}")
        print(f"The cuisine type is: {self.cozinha}")

    def open_restaurant(self):
        """Mostra se o restaurante está aberto ou fechado."""
        print('\nThe restaurant is open...')

    def set_number_served(self):
        """Apresenta o número de clientes servidos."""
        print(f"Clientes atendidos: {self.number_served}")

    def increment_number_served(self, number):
        """método para adicionar o número de clientes servidos"""
        if number < 0:
            print('Não pode retirar o número de pessoas servidas pela pizzaria.')
        else:
                self.number_served += number
                print(f"Agora foi servido no total: {self.number_served} clientes")

# my_restaurant = Restaurant('Marchello', 'pizzaria')
# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()

restaurant = Restaurant('Marchello', 'pizzaria', 10)
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served()
restaurant.increment_number_served(5)


