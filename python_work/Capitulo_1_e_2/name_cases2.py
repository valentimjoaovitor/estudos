'''
2.4 Maiúsculas e Minúsculas: Use uma variável para representar o nome de uma pessoa e, em seguida,
exiba o nome dessa pessoa em letras minúsculas, maiúsculas e as primeiras letras maiúsculas.
'''
nome = input('Coloque um nome para você: ')
nome = nome.upper()
print(nome)

segundo_nome = input('Coloque um segundo nome: ')
segundo_nome = segundo_nome.lower()

print(segundo_nome)

terceiro_nome = input('Coloque um terceiro nome: ')
terceiro_nome = terceiro_nome.title()
print(terceiro_nome)