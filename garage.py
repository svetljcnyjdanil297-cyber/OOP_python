class Garage:
    def __init__(self):
        self.vehicles = []  # Список для хранения любых видов транспорта

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def remove_vehicle(self, vehicle):
        if vehicle in self.vehicles:
            self.vehicles.remove(vehicle)

    def show_all(self):
        for vehicle in self.vehicles:
            print(vehicle.get_info())

    def find_by_brand(self, brand):
        for vehicle in self.vehicles:
            if vehicle.brand.lower() == brand.lower():
                print(vehicle.get_info())