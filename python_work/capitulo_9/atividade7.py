'''Atividade 9.7 Admin página 224'''
class User:
    def __init__(self, first_name, last_name, age, hobbie):

        self.primeiro_nome = first_name
        self.ultimo_nome = last_name
        self.idade = age
        self.hobbie = hobbie

    def describe_user(self):
        self.nome_completo = self.primeiro_nome + ' ' + self.ultimo_nome
        print(f"\nNome de usuário: {self.nome_completo.title()}")
        print(f"Idade: {self.idade}")
        print(f"hobbie: {self.hobbie}")

    def greet_user(self):
        print(f"Seja bem vindo {self.primeiro_nome}!")

class Admin(User):
    def __init__(self, first_name, last_name, age, hobbie):
        super().__init__(first_name, last_name, age, hobbie)
        self.privileges = ['Can add post', 'Can delete post', 'Can ban user', 'Can edit post']

    def show_privileges(self):
        while True:
            i = 1
            print(' ')
            for privilege in self.privileges:              
                print(f'- {i} {privilege}')
                i += 1
            break    

user = Admin('joão', 'valentim', 17, 'program')
user.describe_user()
user.show_privileges()
