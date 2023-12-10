'''Atividade 9.14 da página 233'''
from random import choice
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'l', 'a', 'b', 'd', 'u']

print('Se o seu bilhete conter esse código "2410l" significa que você ganhou um prêmio')

print(str(choice(lista)) + str(choice(lista)) + str(choice(lista)) + str(choice(lista)))
