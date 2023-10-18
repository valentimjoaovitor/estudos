'''
6.8 Animais de estimação: exercício da pag 154
'''

cachorro = {
    'nome': 'cachorro',
    'familia': 'canídeos',
    'que tipo de alimento come': 'onívoros',
    'comportamento': 'amigável',
    'nivel de fofura': 'muito alta',
    
}

gato = {
    'nome': 'gato',
    'familia': 'felinos',
    'que tipo de alimento come': 'carnívoros',
    'comportamento': 'amigável',
    'nivel de fofura': 'fofo'

}

papagaio = {
    'nome': 'papagaio',
    'familia': 'aves',
    'que tipo de alimento come': 'onívoro',
    'comportamento': 'amigável',
    'nivel de fofura': 'fofo'
}

animais_de_estimação = [papagaio, cachorro, gato]

for animal in animais_de_estimação:
    nome = animal['nome']
    familia = animal['familia']
    alimentacao = animal['que tipo de alimento come']
    comportamento = animal['comportamento']
    nivel_de_fofura = animal['nivel de fofura']
    
    print('*-----------------------------------------=-------------------*')
    print(f'\nBichinho de estimação: {nome.title()}')
    print(f'\tfamília: {familia.title()}')
    print(f"\tTipo de alimentação: {alimentacao.title()}")
    print(f'\tComportamento: {comportamento.title()}')
    print(f'\tNível de fofura: {nivel_de_fofura.title()}')