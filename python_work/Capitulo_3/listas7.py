'''
3.7 Reduzindo a lista de convidados: Você acabou de descobrir que sua mesa nova de jantar não chegará
a tempo e agora tem espaço somente para dois convidados.
-Comece com o programa do Exercicio 3.6. Adicione uma linha nova que exiba uma mensagem que você pode convidar
apenas duas pessoas para o jantar.
-Use o pop() para remover convidados da sua lista, um de cada vez, até que restem somente dois nomes nela.
Sempre que remover um nome de sua lista, exiba uma mensagem para essa pessoa informando que lamenta por não
poder convidá-la para o jantar.
-Exiba uma mensagem para cada uma das duas pessoas que ainda estão na sua lista, informando que ainda estão
convidadas.
-Use o del para remover os dois últimos nomes da sua lista, para que ela fique vazia. Exiba sua lista para
ter certeza de que você realmente tem uma lista vazia no final do seu programa.
'''
conv_pessoas = ['Andrews', 'Mily', 'Sara', 'Nico']

quem_nao_vir = conv_pessoas.pop(3)
print(f'perdão {quem_nao_vir} mas não poderei te convidar para o jantar. Outra hora te irei te convidar')

quem_nao_vir = conv_pessoas.pop(2)
print(f'perdão {quem_nao_vir} mas não poderei te convidar para o jantar. Outra hora te irei te convidar')

print(f'Opa {conv_pessoas[0]} você ainda está convidado(a) para o jantar')
print(f'Eai {conv_pessoas[1]} você ainda está convidado(a) para o jantar')

del conv_pessoas[0]
del conv_pessoas[0]
print(conv_pessoas)


