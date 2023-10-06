"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
#como eu resolvi
#valor = input('coloque um valor inteiro: ')
#if (int(valor) %  2) == 0:
#    print('O número é par')
#else:
#    print('O valor é impar')

#como o professor resolveu
#entrada = input('Digite um número: ')

# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto = 'par'

#     print(f'O número {entrada_int} é {par_impar_texto}')
# else:
#     print('Você não digitou um número inteiro')

#try:
#    entrada_int = float(entrada)
#    par_impar = entrada_int % 2 == 0
#    par_impar_texto = 'ímpar'
#
#    if par_impar:
#        par_impar_texto = 'par'
#
#    print(f'O número {entrada_int} é {par_impar_texto}')
#except:
#    print('Você não digitou um número inteiro')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
#entrada = input('Coloque a hora em números inteiros: ')

#try:
#    hora = int(entrada)

#    if hora >= 0 and hora <= 11:
#        print('bom dia')
#    elif hora >= 12 and hora <=17:
#        print('Boa tarde')
#    elif hora >= 18 and hora <=23:
#        print('boa noite!')
#    else:
#        print('não conheço esse número')
#except:
#    print('por favor, coloque apenas números inteiros')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

#nome_de_usuario = input('coloque o seu primeiro nome aqui: ')

#if len(nome_de_usuario) <=4:
#    print('seu nome é curto')
#elif len(nome_de_usuario) >=5 and len(nome_de_usuario) <=6:
#    print('Seu nome é normal')
#else:
#    print('seu nome é muito grande')

#resolução do professor
#nome = input('Digite seu nome: ')
#tamanho_nome = len(nome)

#if tamanho_nome > 1:
#    if tamanho_nome <= 4:
#        print('Seu nome é curto')
#    elif tamanho_nome >= 5 and tamanho_nome <= 6:
#        print('Seu nome é normal')
#    else:
#        print('Seu nome é muito grande')
#else:
#    print('Digite mais de uma letra.')