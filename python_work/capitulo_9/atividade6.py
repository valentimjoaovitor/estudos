"""Atividade 9.6 sorveteria página 224"""
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

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['menta', 'chocolate', 'morango', 'flocos', 'ovomaltine']

    def show_flavors(self):
        print('Lista de Sabores:')
        for flavor in self.flavors:
            print(f"\t-{flavor}")
    
    def select_flavor(self):
        
        while True:
            escolha = input('Qual tipo de sabor você quer para o seu sorvete? ')

            if escolha not in self.flavors:
                print('\nEsse sabor não está na lista, escolha outro.')
                continue

            else:
                print(f"Tome aqui o seu sorvete de {escolha.title()}")
                break

sabores = IceCreamStand('SorveteriaIce', 'Sorveteria')
sabores.show_flavors()
sabores.select_flavor()
