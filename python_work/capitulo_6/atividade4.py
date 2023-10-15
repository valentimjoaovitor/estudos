'''
atividade 6.4 Glossário 2 pag 147  (não entendi direito o que se tá pedindo)
'''

glossario = {
    'simples é melhor que complexo': 5,
    'complexo é melhor que complicado': 10,
    'explicito é melhor que implicito': 7,
    'bonito é melhor que feio': 8,
    'se a ideia é facil de explicar então é uma boa ideia': 10
}

for frase, value in glossario.items():
    print(f'\nfrase: {frase}')
    print(f'nota: {value}')
