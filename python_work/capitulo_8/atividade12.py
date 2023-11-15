'''
Atividade 8.12 Sanduíches: página 187
'''
def lista_sanduinche(*ingredientes):
    print("\nIngredientes que estão no sanduíche:")
    for ingrediente in ingredientes:
        print(f"- {ingrediente}")


lista_sanduinche('mortadela', 'tomate', 'salsicha')
lista_sanduinche('queijo')
lista_sanduinche('alface', 'tomate')