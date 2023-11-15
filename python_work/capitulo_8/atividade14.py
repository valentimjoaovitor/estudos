'''
8.14 Carros página 197
'''
def info_carros(fabricante, nome_modelo, **valores):
    valores['fabricante'] = fabricante
    valores['Modelo_do_carro'] = nome_modelo
    return valores

    

carro = info_carros('subaru', 'outback', color='blue', tow_package='True')
print(carro)