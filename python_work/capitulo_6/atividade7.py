'''
6.7 atividade python pag 154
'''
user1 = {
    'first_name': 'joao',
    'last_name': 'valentim',
    'age': 17,
    'city': 'indaiatuba',
}

user2 = {
    'first_name': 'maria',
    'last_name': 'silva',
    'age': 18,
    'city': 'rio de janeiro',
}

user3 = {
    'first_name': 'pedro',
    'last_name': 'alberto',
    'age': 20,
    'city': 'são paulo',
}

users = [user1, user2, user3]

for user in users:
    full_name = f"\n{user['first_name']} {user['last_name']}"
    dados = f"idade: {user['age']} \tcidade: {user['city']}"
    
    print(full_name.title())
    print(dados.title())

