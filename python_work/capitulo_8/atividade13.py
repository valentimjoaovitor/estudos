'''
atividade 8.13 Perfil de usuário: página 197
'''
def build_profile(first, last, **user_info):
    """cria um dicionário contendo tudo o que sabemos sobre um usuário"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='priceton',
                             fild='physics')
print(user_profile)

meu_perfil = build_profile('João', 'Valentim', 
                           cidade='Indaiatuba',
                           estado='São Paulo')
print(meu_perfil)