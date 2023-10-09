'''
5.6 exercício da página 124
'''

age = int(input('how old are you? '))

if age < 2:
    print('You are a baby.')

elif age >= 2 and age < 4:
    print('You are a child.')

elif age >= 4 and age < 13:
    print('You are a boy or a girl.')

elif age >= 13 and age < 20:
    print('You are a teen.')

elif age >= 20 and age < 65:
    print('you are a adult.')

else:
    print('You are elderly.')