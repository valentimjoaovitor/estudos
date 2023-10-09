'''
pag 128 atividade 5.8 Olá admin...
'''
usuarios = ['admin', 'joao', 'ana',
            'jorge', 'samuel', 'larissa']

for usuario in usuarios:
    if usuario == 'admin':
        print('Olá administrador, gostaria'
              ' de ver um relatório de status?')
    else:
        print(f'\nOlá {usuario} obrigado por fazer login novamente.')

