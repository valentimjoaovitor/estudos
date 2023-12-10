'''Atividade 9.13 Dados: página 233'''
from random import randint

class Die:
    def __init__(self, sides=6 ):
        self.sides = sides

    def rodar_dado(self):
        dado = randint(1, self.sides)
        print(dado)

my_die = Die()
print(f'O valor do dado foi: \t'), my_die.rodar_dado()