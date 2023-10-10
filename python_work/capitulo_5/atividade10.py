'''
atividade 5.10 página 129
'''

# current_users = ['joao', 'maria', 'pedro', 'gabriel']
# new_users = ['joao', 'larissa', 'pedro', 'enzo']

# for new_user in new_users:
#     if new_user in current_users:
        
#         print('Esse usuário ja existe coloque um novo')
        
#     else:
#         print('usuário válido')

#outra solução!!

current_users = ['joao', 'maria', 'pedro', 'gabriel']
new_users = ['joao', 'larissa', 'pedro', 'enzo']

i = 0

for new_user in new_users:

    if new_user == current_users[i]:
        i += 1
        print('Esse usuário ja existe coloque um novo')
        
    else:
        print('usuário válido')
        i += 1