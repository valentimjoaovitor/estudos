'''
6.11 Cidades: atividade pag 155 curso intensivo de python
'''

cities = {
    'indaiatuba': {
        'country': 'brazil',
        'population': 256.223,
        'fact': "it's bautiful"
    },

    'espirito santo': {
        'country': 'brazil',
        'population': 3_000_000,
        'fact': 'wakanda'
    },

    'porto alegre': {
        'country': 'brazil',
        'population': 1_000_000,
        'fact': 'burguês'
    }
}

for city, info in cities.items():
    country = info['country']
    population = info['population']
    fact = info['fact']

    print(f'\nName of the city: {city}')
    print(f'\tCountry: {country}')
    print(f'\tPopulation: {population}')
    print(f'\tCurious fact: {fact}')
    

