from models.vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, has_sidecar):
        super().__init__(brand, model, year)
        self.has_sidecar = has_sidecar

    def get_info(self): 
        base_info = super().get_info()
        sidecar_status = "Да" if self.has_sidecar else "Нет"
        return f'{base_info} {self.has_sidecar}'

    def move(self):
        sidecar_text = "с коляской" if self.has_sidecar else "без коляски"
        return f"Мотоцикл {self.brand} {sidecar_text}"
