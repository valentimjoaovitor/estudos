'''
6.9 lugares favoritos: atividade pag 154
'''

favorite_places = {
    'joao': 'ecologic park',
    'pedro': 'restaurant',
    'ana': 'mall'

}

for name, favorite_place in favorite_places.items():
    print(f'\tName: {name.title()}')
    print(f'\tFavorite Place: {favorite_place.title()}')
    print('-----------------------------(*)---------------------------------')