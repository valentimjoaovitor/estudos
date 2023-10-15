'''
6.1 atividade pag 140
'''

dados = {'first_name': 'joão vitor',
         'last_name': ' valentim',
         'age': 17,
         'city': 'indaiatuba'         
         
         }
nome = dados['first_name']
ultimo_nome = dados['last_name']
idade = dados['age']
cidade = dados['city']

nome_completo = nome + ultimo_nome

print(nome_completo.title())
print(idade)
print(cidade.title())