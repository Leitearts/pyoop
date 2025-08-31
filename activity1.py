# Parent class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.__battery = 100  # private (encapsulation)

    def call(self, number):
        return f"{self.model} is calling {number}..."

    def check_battery(self):
        return f"Battery level: {self.__battery}%"

    def charge(self, amount):
        self.__battery = min(100, self.__battery + amount)
        return f"Battery charged to {self.__battery}%"

# Child class (inheritance)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, gpu):
        super().__init__(brand, model, storage)
        self.gpu = gpu

    def play_game(self, game):
        return f"{self.model} is running {game} smoothly with {self.gpu} GPU!"
    

# Using the classes
phone1 = Smartphone("Samsung", "Galaxy S23", "256GB")
gaming1 = GamingPhone("Asus", "ROG Phone 7", "512GB", "Adreno 740")

print(phone1.call("+254700000000"))
print(phone1.check_battery())
print(gaming1.play_game("Call of Duty Mobile"))
