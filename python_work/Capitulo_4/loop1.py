'''
4.1 Pizzas: Pense em, pelo menos, três tipos que você gosta. Armazene esses nomes de pizza em uma lista
e use o loop for para exibir o nome de cada uma.
-Modifique seu loop for a fim de que exiba uma frase usando o nome da pizza, em vez de exibir apenas o nome
da pizza. Para cada pizza, você deve gerar uma linha de saída com uma simples afirmação como: Gosto de
pizza de pepperoni.
-Adicione uma linha no final do seu programa, fora do loop for, que ressalte o quanto você gosta de pizza.
A saída deve ter três ou mais linhas sobre os tipos de pizza que você gosta e, em seguida, uma frase adicional,
como Eu amo pizza!
'''

tipos_pizza = ['pepperoni', 'portuguesa', 'frango']

for pizza in tipos_pizza:
    print(f'Eu gosto do sabor da pizza de: {pizza.title()}\n')

print('eu adoro pizza por causa que é muito bom')
print('eu adoro pizza por ser muito saborosa')
print('eu adoro pizza por causa que é bom')

print('Eu amo pizza!')
