valor1 = input('coloque o primeiro valor: ')
valor2 = input('coloque o segundo valor: ')

if valor1 > valor2:
    print(f"O primeiro valor '{valor1}' é maior que o segundo valor '{valor2}'")

elif valor2 > valor1:
    print(f"o segundo valor '{valor2}' é maior que o primeiro valor '{valor1}'")

else:
    print("os dois valores são iguais")