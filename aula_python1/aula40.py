'''Calculadora com o while'''

while True:
    numero1 = input('coloque um numero: ')
    numero2 = input('Coloque um segundo numero: ')
    operador = input('selecione um operador (+ - / *): ')

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero1)
        num_2_float = float(numero2)
        numeros_validos = True

    except:
        numeros_validos = None
        
        if numeros_validos is None:
            print('Um ou ambos os números digitados são inválidos.')
            continue
    
    operadores_permitidos = '+-*/'

    if operador not in operadores_permitidos:
        print('operador inválido.')
        continue

    if len(operador) > 1:
        print('digite apenas 1 operador.')

###
    print('Realizando a conta, confira o resultado abaixo.')
    if operador == '+':
        print(f'A soma dos numeros {num_1_float} e {num_2_float} é: {num_1_float + num_2_float}')

    elif operador == '-':
        print(f'A subtração dos numeros {num_1_float} e {num_2_float} é: {num_1_float - num_2_float}')

    elif operador == '*':
        print(f'A multiplicação dos numeros {num_1_float} e {num_2_float} é: {num_1_float + num_2_float}')

    elif operador == '/':
        print(f'A divisão dos numeros {num_1_float} e {num_2_float} é: {num_1_float + num_2_float}')

    else:
        print('você nunca deveria chegar aqui.')

    sair = input('Você quer sair? pressione [s]im: ').lower().startswith('s')
    

    if sair is True:
        break