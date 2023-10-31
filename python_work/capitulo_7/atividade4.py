'''
atividade 7.4 Ingredientes de cinema pagina 168
'''

ingredient = '\nColoque os ingredientes que você quer na pizza'
ingredient += "\n(digite 'quit' para sair do programa.) "
    
while True:
    cobertura = input(ingredient)

    if cobertura == 'quit':
        break
    else:
        print(f'Adicionando {cobertura} a pizza')

