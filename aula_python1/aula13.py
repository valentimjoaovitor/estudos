nome = 'João Vitor Valentim'
altura = 1.70
peso = 60
imc = peso / (altura * altura)

'f-strings' # 'f' significa formatação.
linha1 = f'{nome} tem {altura:.2f} de altura'
                            #^diz quantas casas decimais pode mostrar
linha2 = f'pesa {peso} quilos e seu imc é: '
linha3 = f'{imc:.2f}'

print(nome)
print(linha1)
print(linha2)
print(linha3)
print('')