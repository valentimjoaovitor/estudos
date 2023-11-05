# Argumentos posicionais
def describe_pet(animal_type, pet_name):
    '''Exibe as informações sobre um animal de estimação'''
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')
describe_pet('dog', 'willie')
