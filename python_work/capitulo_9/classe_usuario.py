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