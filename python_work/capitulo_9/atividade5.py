'''
Atividade 9.5 Tentativa de login: página 216
'''

class User:
    def __init__(self, first_name, last_name, age, hobbie):

        self.primeiro_nome = first_name
        self.ultimo_nome = last_name
        self.idade = age
        self.hobbie = hobbie
        self.login_attempts = 0

    def describe_user(self):
        self.nome_completo = self.primeiro_nome + ' ' + self.ultimo_nome
        print(f"\nNome de usuário: {self.nome_completo}")
        print(f"Idade: {self.idade}")
        print(f"hobbie: {self.hobbie}")

    def greet_user(self):
        print(f"Seja bem vindo {self.primeiro_nome}!")

    def increment_login_attempts(self, attemps= 1):
        self.login_attempts += attemps
        print(f"Tentativas de login: {self.login_attempts}")

    def reset_login_attempts(self, reset= 0):
        self.login_attempts = reset
        print(f"Suas tentativas de login foram resetadas para {self.login_attempts}")

login = User('João', 'Valentim', 17, 'estudar')

login.increment_login_attempts()
login.increment_login_attempts()
login.increment_login_attempts()
login.increment_login_attempts()
login.increment_login_attempts()
login.increment_login_attempts()

login.reset_login_attempts()
login.increment_login_attempts()