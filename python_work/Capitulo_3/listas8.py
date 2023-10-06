'''
3.8 Conhecendo o mundo: Pense em pelo menos cinco lugares do mundo que você gostaria de conhecer
-Armazene esses locais em uma lista. Verifique se ela não está em ordem alfabética.

-Exiba sua lista na ordem original. Não se preocupe em exibir a lista ordenadamente; basta exibi-la

como uma lsta crua do python.
-Use sorted() para exibir sua lista em ordem alfabética, sem alterar a lista original.

-Mostre que sua lista ainda está na ordem original exibindo-a

-Use o sorted() para exibir sua lista em ordem alfabética reversa, sem alteerar a ordem original dela.

-Demonstre que sua lista ainda está na ordem original exibindo-a mais uma vez.

-Use o reverse() para alterar a ordem de sua lista. Exiba essa lista para mostrar que sua ordem foi
alterada.

-Use o reverse() para alterar a ordem de sua lista novamente. Exiba-a a fim de mostar que voltou à ordem original.

-Use o sort() para alterar sua lista para que ela seja armazenada em ordem alfabética. Exiba a lista para mostrar
que sua ordem foi alterada

-Use sort() para alterar sua lista, de modo que ela seja armazenada em ordem alfabética inversa. Exiba a lista
para mostrar que sua ordem foi alterada.
'''

lugares = ['Canada', 'Nova York', 'Estados Unidos', 'Antartica', 'Paris']
print(lugares, 1) #primeiro print

print(sorted(lugares),2, 'ordem alfabética') #segundo print

print(lugares, 3) #terceiro print

print(sorted(lugares, reverse= True), 4) #quarto print

print(lugares, 5) #quinto print

lugares.reverse()
print(lugares, 6) #sexto print
lugares.reverse()
print(lugares, 7) #sétimo print

lugares.sort()
print(lugares, 8) #oitavo print

lugares.sort(reverse= True) #nono print
print(lugares, 9)