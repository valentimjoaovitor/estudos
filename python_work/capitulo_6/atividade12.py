'''
6.12 extensões atividade pag 155 livro curso intensivo de python
Agora que já estamos trabalhando com exemplos complexos o suficiente para que sejam mais
desenvolvidos de diferentes maneiras, use um dos programas de exemplo deste capítulo e o amplie,
adicionando chaves e valores novos, alterando o contexto do programa ou melhorando a formatação da
saída.
'''

people = {
    'joão vitor': {
        'age': 17,
        'height': 1.70,
        'hobbie': 'read books'
    },
    'pedrin': {
        'age': 20,
        'height': 1.90,
        'hobbie': 'play video games'
    },
    'addam': {
        'age': 16,
        'height': 1.68,
        'hobbie': 'watch anime'
    }
}

for person, info in people.items():
    age = info['age']
    height = info['height']
    hobbie = info['hobbie']

    print(f'\nName: {person.title()}')
    print(f'\tAge: {age}')
    print(f'\tHeight: {height}')
    print(f'\tHobbie: {hobbie.title()}')


