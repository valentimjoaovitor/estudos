"""Conjunto de classes que pode ser usado para repreentar carros elétricos"""

from car import Car

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

class ElectricCar(Car):
    """Representa aspectos de um carro, específicos para veículos elétricos"""

    def __init__(self, make, model, year):
        """
        Inicializa os atributos da classe-pai.
        Em seguida, inicializa os atributos específicos para um carro elétrico. 
        """
        super().__init__(make, model, year)
        self.battery = Battery()