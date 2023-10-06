'''
3.1 Nomes: Armazene o nome de alguns de seus amigos em uma lista chamada 'names'. Exiba
o nome de cada pessoa acessando cada elemento da lista, de cada vez.
'''
#Na lista vai de 0 a 6.
names = ['Andrews', 'Jamily', 'Nicolas', 'Sara', 'Matheus', 'Isac', 'Larissa']
i = int(input('Coloque um número para ver qual nome de um amigo seu irá cair de 1 a 7: ')) - 1

#Fiz esse if para caso a pessoa coloque um número que não seja possivel
if i < 0:
    print('O programa só vai funcionar se você colocar um valor válido!')

else:
    print(names[i])
