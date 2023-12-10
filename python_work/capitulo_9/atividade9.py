'''Atividade 9.9 Trocar bateria página 224'''
import time

class Car:
    """Simples tentativa de representar um carro"""

    def __init__(self, make, model, year):
        """Inicializa os atributos para descrever um carro"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Retorna um nome descritivo, formatado elegantemente"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Exibe uma frase mostrando a quilometragem do carro"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Define a leitura do hodômetro para o valor fornecido"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Adiciona a quantidade fornecida à leitura do hodômetro"""
        self.odometer_reading += miles

class Battery:
    """Simples tentativa de modelar uma bateria para um carro elétrico"""
    
    def __init__(self, battery_size=40):
        """Inicializa os atributos da bateria"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Exibe uma frase descrevendo o tamanho da bateria"""
        print(f"This car has a {self.battery_size}- kWh battery")

    def get_range(self):
        """Exibe frase sobre a distância que o carro percorre com essa bateria"""
        if self.battery_size == 40:
            range = 150

        elif self.battery_size == 65:
            range = 225
        
        print(f"this car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size == 40:
            self.battery_size = 65
            print('fazendo upgrade em sua bateria.')


class ElectricCar(Car):
    """Representa aspectos de um carro, específicos para veículos elétricos"""

    def __init__(self, make, model, year):
        """
        Inicializa os atributos da classe-pai.
        Em seguida, inicializa os atributos específicos para um carro elétrico. 
        """
        super().__init__(make, model, year)
        self.battery = Battery()

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()

print('aguarde 5 segundos para melhorarmos a bateria de seu carro...')
time.sleep(5)

my_leaf.battery.get_range()
print(' ')