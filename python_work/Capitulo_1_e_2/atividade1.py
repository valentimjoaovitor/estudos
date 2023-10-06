'''
Faça um Programa que leia três números e mostre o maior deles.
'''
 
print('Bem-Vindo ao programa')
print('Coloque três valores e iremos falar que é o maior número!')
print(' ')
 
valor1 = int(input('Coloque o primeiro valor: '))
valor2 = int(input('Coloque o segundo valor: '))
valor3 = int(input('Coloque o terceiro valor: '))
print(' ')
 
 
print('RESULTADO CALCULADO COM SUCESSO, AQUI ESTÁ SUA ORDEM. ')
print(' ')
if valor1 > valor2 and valor1 > valor3:
    print('1 O primeiro maior é: ', valor1)
    if valor2 > valor3:
        print('1 O segundo maior é: ', valor2)
        print('1 E o menor é: ', valor3)
    elif valor3 > valor2:
        print('1 O segundo maior é:', valor3)
        print('1 E o menor é: ', valor2)
   
if valor2 > valor1 and valor2 > valor3:
    print('2 O primeiro maior é: ', valor2)
    if valor1 > valor3:
        print('2 O segundo maior é: ', valor1)
        print('2 E o menor é: ', valor3)
    elif valor3 > valor1:
        print('2 O segundo maior é:', valor3)
        print('2 E o menor é: ', valor1)
     
if valor3 > valor1 and valor3 > valor2:
    print('3 O primeiro maior é: ', valor3)
    if valor2 > valor1:
        print('3 O segundo maior é: ', valor2)
        print('3 E o menor é: ', valor1)
    elif valor1 > valor2:
        print('3 O segundo maior é:', valor1)
        print('3 E o menor é: ', valor2)
