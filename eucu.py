class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")


class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Number of doors: {self.num_doors}")


class Bike(Vehicle):
    def __init__(self, brand, model, year, type):
        super().__init__(brand, model, year)
        self.type = type

    def display_info(self):
        super().display_info()
        print(f"Bike type: {self.type}")


# Example usage
car = Car("Toyota", "Camry", 2020, 4)
car.display_info()

bike = Bike("Honda", "CBR500R", 2019, "Sport")
bike.display_info()
