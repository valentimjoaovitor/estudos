'''
2.7 Removendo nomes: Use uma variável para representar o nome de uma pessoa e inclua alguns caracteres
de espaço em branco no início e no final do nome. Lembre-se de usar cada combinação de caracteres, "\t" e "\n",
pelo menos uma vez. Exiba o nome uma vez para que o espaço em branco ao redor do nome seja mostrado. Em seguida,
printe o nome usando cada uma das três funções de remoção, lstrip(), rstrip(), e strip().

'''

nome = '\tJoão Vitor Valentim       '
print(nome, 'normal version') #sem nenhuma função para modificar
print(nome.lstrip(), 'left')  #tirou o espaço do lado direto
print(nome.rstrip(), 'right') #tirou o espaço do lado esquerdo
print(nome.strip(), 'both') #tirou o espaço de ambos os lados