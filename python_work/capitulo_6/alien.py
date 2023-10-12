# alien_0 = {'color': 'green', 'points': 5}

# print(alien_0['color'])
# print(alien_0['points'])

# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)

# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

# # començando com um dicionário vazio
# alien_0 = {}

# alien_0['color'] = 'green'
# alien_0['points'] = 5
# print(alien_0)

# modificando valores de um dicionário:
# alien_0 = {'color': 'green'}
# print(f'The alien is {alien_0["color"]}')

# alien_0['color'] = 'yellow'
# print(f"The alien is now {alien_0['color']}")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f'Oiginal position: {alien_0["x_position"]}')

# Desloca o alienígena para a direita
# Estipula a distância que o alienigena deve percorrer conforma sua velocidade

if alien_0['speed'] == 'slow':
    x_increment = 1

elif alien_0['speed'] == 'medium':
    x_increment = 2

else:
    # Com isso, o alinígena fica veloz
    x_increment = 3

# A posição nova é a posição antiga mais o incremento
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f'New position: {alien_0["x_position"]}')
