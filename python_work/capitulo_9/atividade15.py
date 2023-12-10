'''Atividade 9.15 Análise de loteria, página 233'''
from random import choice

my_ticket = [
            1, 2, 3, 4, 5, 6,
             7, 8, 9, 10, 'l',
            'a', 'b', 'd', 'u'
            ]
vencedor = '1023uu'

i = 0
while True:
    i += 1
    a, b, c, d, e = choice(my_ticket), choice(my_ticket), choice(my_ticket), choice(my_ticket), choice(my_ticket)
    participante = str(a) + str(b) + str(c) + str(d) + str(e)
    
    if participante == vencedor:
        print('Encontramos um premiado')
        print(f'O valor vencedor é "{vencedor}", o código encontrado foi {participante}')
        print(f'esse código rodou: {i} vezes')
        break