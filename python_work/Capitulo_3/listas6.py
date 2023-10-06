'''
3.6 Mais convidados: Você acabou de encontrar uma mesa maior de janta, agora há mais espaço disponível.
Convide mais três pessoas para o jantar.
-Comece com o programa do exercício 3.4 ou 3.5. No final do programa, adicione um print(), informando
às pessoas que encontrou uma mesa maior.
-Use um insert() para adicionar um convidado novo ao ínicio de sua lista.
-Use um insert() para adicionar um convidado novo no meio de sua lista.
-Use um append() para adicionar um convidado novo no final de sua lista.
-Exiba um conjunto novo de mensagens de convite, um para cada pessoa em sua lista
'''

conv_pessoas = ['Andrews', 'Mily', 'Sara', 'Nico']

print('Eu encontrei uma mesa maior para mais pessoas!')

conv_pessoas.insert(0, 'Larissa')
conv_pessoas.insert(2, 'João')
conv_pessoas.append('Matheus')

i = int(input('Coloque um número para enviar a carta para um amigo: '))

print(f'Eai {conv_pessoas[i]}, esse é um convite novo para você! Venha jantar em minha casa.')


