'''
3.4 Lista de convidados: Se pudesse convidar qualquer pessoa, viva ou falecida, para um jantar, quem você
convidaria? Crie uma lista que tenha pelo menos três pessoas que gostaria de convidar para um jantar. Em
seguida, use sua lista a fim de exibir uma mensagem para cada pessoa, convidando-a para o jantar.
'''
#indice:           0         1        2       3 
conv_pessoas = ['Andrews', 'Mily', 'Sara', 'Nico']
i = int(input('Escolha um nome de um amigo para aparecer na carta: '))
print(f'Eai {conv_pessoas[i]}, estou te convidando para uma pequena festa na minha casa. Vem cá!')