

class Cars:
    def __init__(self, make, model, color, year):
        self.make = make
        self.model = model
        self.color = color
        self.year = year

    def description(self):
        print(f"The Car Make is: {self.make}, Model: {self.model}, Color: {self.color}, Year: {self.year}")


mycar = Cars("Toyota", "Camry", "Red", 2020)
mycar.description()
mycar = Cars("Honda", "Civic", "Blue", 2019)
mycar.description()
mycar = Cars("Ford", "Mustang", "Black", 2021)
mycar.description()
mycar = Cars("Dodge", "Charger", "White", 2018)
mycar.description()
mycar = Cars("Nissan", "Skyline", "Silver", 2022)
mycar.description()





