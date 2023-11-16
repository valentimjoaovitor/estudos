import printing_functions

objetos_nao_printados = ['controle remoto', 'carrinho',
           'boneca de brinquedo', 'urso de pelúcia']
objetos_printados = []

printing_functions.print_models(objetos_nao_printados, objetos_printados)
printing_functions.show_completed_models(objetos_printados)





# ---------------------------------------------------------------
# Começa com alguns design que precisam ser impressos
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# Simula a impressão e cada design, até que não reste nenhum
# Passa cada design para completed_models após impressão
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f'Printing model: {current_design}')
#     completed_models.append(current_design)

# Exibe todos os modelos concluídos
# print('\nThe following model have been printed:')
# for completed_model in completed_models:
#     print(completed_model)

# def print_models(unprinted_designs, completed_models):
#     """
#     Simula a impressão de cada design, até que não reste nenhum.
#     Passa cada design para completed_models após impressão.
#     """
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing model: {current_design}")
#         completed_models.append(current_design)

# def show_completed_models(completed_models):
#     '''Exibe todos os modelos impressos'''
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)

# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)
