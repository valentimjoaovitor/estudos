'''
9.3 Usuários: Atividade da página 211
'''

class User:
    def __init__(self, first_name, last_name, age, hobbie):

        self.primeiro_nome = first_name
        self.ultimo_nome = last_name
        self.idade = age
        self.hobbie = hobbie

    def describe_user(self):
        self.nome_completo = self.primeiro_nome + ' ' + self.ultimo_nome
        print(f"\nNome de usuário: {self.nome_completo}")
        print(f"Idade: {self.idade}")
        print(f"hobbie: {self.hobbie}")

    def greet_user(self):
        print(f"Seja bem vindo {self.primeiro_nome}!")

usuario = User('João', 'Valentim', 17, 'program')
usuario.describe_user()
usuario.greet_user()

usuario2 = User('Jeto', 'malencio', 15, 'futebol')
usuario2.describe_user()
usuario2.greet_user()

usuario3 = User('gilberto', 'nabetor', 20, 'academia')
usuario3.describe_user()
usuario3.greet_user()