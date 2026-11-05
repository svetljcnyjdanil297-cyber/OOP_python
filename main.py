import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from models.car import Car
from models.truck import Truck
from models.motorcycle import Motorcycle
from garage import Garage
from models.electric_car import ElectricCar


def main():
    my_garage = Garage()
    car = Car("Toyota", "Camry", 2022, doors=4)
    my_garage.add_vehicle(car)
    my_garage.show_all()
    tesla = ElectricCar("Tesla", "Model S", 2024, 100, "12.5")
    my_garage.add_vehicle(tesla)

if __name__ == "__main__":
    main()
