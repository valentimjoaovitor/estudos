def greet_users(names):
    '''Exibe um simples hello para caa usuário na lista'''
    for name in names:
        msg = f"hello, {name.title()}"
        print(msg)

usernames = ['hanna', 'ty', 'margot']
greet_users(usernames)