'''
3.5 Mudando a lista de convidados: Você acabou de ficar sabendo que um dos convidados não conseguirá
ir ao jantas, assom precisa enviar um conjunto novo de convites. É necessário convida outra pessoa.

-Comece com o programa do exercício 3.4. No final do progama, adicione um print(), informando o nome
do convidado que não irá ao jantar.
-Modifique sua lista substituindo o nome do convidado que não pode comparecer pelo nome da pessoa nova
que você está convidando.
-Exiba um segundo conjunto de mensagens de convite, uma para cada pessoa que ainda não consta em sua lista.
'''

conv_pessoas = ['Andrews', 'Mily', 'Sara', 'Nico']
print(conv_pessoas)
print('A Sara não vai poder aparecer à janta')

conv_pessoas[2] = 'Felipe'
print(conv_pessoas)

novas_pessoas = ['Rafael', 'João', 'Larissa', 'Gustavo']
i = int(input('coloque um número para imprimir um nome na carta: '))

print(f'eai {novas_pessoas[i]} estou convidando você para uma janta em minha casa.')
