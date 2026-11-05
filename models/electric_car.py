from models.vehicle import Vehicle

class ElectricCar(Vehicle):
    def __init__(self, brand, model, year, battery_capacity, autopilot_version):
        super().__init__(brand, model, year)
        self.battery_capacity = battery_capacity 
        self.autopilot_version = autopilot_version 

    def get_info(self):
        return f"{super().get_info()}  {self.battery_capacity} {self.autopilot_version}"

    def move(self):
        return f"Электромобиль {self.brand} "
