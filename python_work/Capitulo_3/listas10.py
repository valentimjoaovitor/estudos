'''
3.10 Funções: Pense em coisas que você conseguiria armazenar em uma lista. Por exemplo, você pode criar uma
lista de montanhas, rios, países, cidades, idiomas, ou qualquer outra coisa que quiser. Crie um programa
com uma lista contendo esses itens e, em seguida, use cada função apresentada nesse capitulo, pelo menos uma
vez.
'''
idiomas = ['português', 'inglês', 'espanhol', 'japonês', 'chinês', 'coreano', 'latin', 'fracês', 'russo']
message = f'Os idiomas que conheço são: {idiomas[1].title()}'
print(idiomas)
print(idiomas[0])
print(idiomas[0].title())
print(idiomas[-1])
print(message)

print(' ')

idiomas[3] = 'angolano' #trocando um valor
print(idiomas)

print(' ')

idiomas.append('japonês')  # anexando um valor
print(idiomas)

print(' ')

idiomas.insert(1, 'mandarim')  # inserindo um valor
print(idiomas)

print(' ')

del idiomas[1]
print(idiomas)

idi_reserva = idiomas.pop(4)
print(idiomas)
print(idi_reserva, 'foi removido da lista principal')

print(' ')
esqueci = f'O idiomas que esqueci foi {idi_reserva}'
print(esqueci)

idiomas.sort()
print(idiomas)  #ordem alfabética

print(' ')
idiomas.sort(reverse=True) #ordem alfabética invertida
print(idiomas)

idiomas.reverse()
print(idiomas)
