'''
atividade 8.5 página 183
'''

def describe_city(nome='Reykjavik', pais='Islândia'):
    print(f"\nnome da cidade: {nome.title()}")
    print(f"a cidade fica localizada no(a): {pais.title()}")

describe_city()
describe_city('Reiquiavique')
describe_city(nome='são paulo', pais='brasil')