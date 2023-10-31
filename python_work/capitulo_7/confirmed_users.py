# Começa com usuários que precisam ser verificados,
# e uma lista vazia a fim de armazenar os usários confirmados
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# faz a verificação de cada usuário até que não se tenha mais
# usuários não confirmados
# Transefere cada usuário verificado para a lista de usuários confirmardos
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f'Verifying user: {current_user.title()}')
    confirmed_users.append(current_user)

# Exibe todos os usuários confirmados
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())