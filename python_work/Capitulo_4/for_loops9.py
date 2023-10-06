'''
4.9 Cube Comprehension> Use umma list comprehension para gerar uma lista dos 10 primeiros cubos.
'''

cubos = [cubo**3 for cubo in range(1, 11)]  # List comprehension é literalmente um loop for em uma
print(cubos)                                # lista, no caso tudo em uma única linha.