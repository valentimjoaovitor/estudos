"""
Iterando strings com while
"""
#minha versão
#nome = input('Coloque o seu nome aqui: ')
#contador = 0


#while contador < len(nome):
#    print('*', nome[contador], '*')
#    contador += 1

 #resolução
    
"""
Iterando strings com while
"""
#       012345678910
# nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321

#exemplo
nome = 'Maria Helena'  # Iteráveis

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)