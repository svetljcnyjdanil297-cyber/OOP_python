from models.vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, brand, model, year, max_load):
        super().__init__(brand, model, year)
        self.max_load = max_load

    def get_info(self): 
        base_info = super().get_info()
        return f'{base_info} {self.max_load}'

    def move(self):
        return f"Грузовик {self.brand} {self.max_load}"
