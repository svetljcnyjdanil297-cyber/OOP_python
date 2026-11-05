from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self._speed = 0
    @property
    def speed(self):
        return self._speed
    @speed.setter
    def speed(self, value):
        if value < 0:
            raise ValueError("Скорость не может быть отрицательной!")
        self._speed = value

    def characteristics(self):
        return (self.brand, self.model, self.year, self._speed)

    def accelerate(self, value):
        self.speed += value

    def brake(self, value):
        self.speed -= value
        if self.speed < 0:
            self.speed = 0

    def stop(self):
        self._speed = 0
    @abstractmethod
    def get_info(self):
            return (f'{self.brand} {self.model} {self.year} {self._speed}')
    @abstractmethod
    def move(self):
        pass
    def __str__(self):
        return (f'{self.brand} {self.model} {self.year} {self._speed}')
