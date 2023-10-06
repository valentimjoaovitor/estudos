'''
3.2 Cumprimentos: Comece com a lista usada no exercício 3.1, mas desta vez de apenas exibir o nome
de cada pessoa, exiba também uma mensagem para elas. O texto de cada mensagem deve ser o mesmo, porém,
cada mensagem deve ser personalizada com o nome da pessoa.
'''

names = ['Andrews', 'Jamily', 'Nicolas', 'Sara', 'Matheus', 'Isac', 'Larissa']
i = int(input('Coloque um número para ver qual nome de um amigo seu irá cair de 1 a 7: ')) - 1

message = 'O número que você escolheu representa o seu amigo(a): '

print(' ')
print(message + str(names[i]))
print('')