import classe_usuario

class Admin(classe_usuario.User):
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

class Privileges(Admin):
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