class Car:
    def __init__(self, make: str, model: str, year: int, engine_volume: float,
                 fuel_efficiency_l_per_100km: int or float):
        self.make = make
        self.model = model
        self.year = year
        self.engine_volume = engine_volume
        self.fuel_efficiency_l_per_100km = fuel_efficiency_l_per_100km
    def __str__(self):
        return (f"Автомобіль: {self.year} {self.make} {self.model}, об'єм двигуна: {self.engine_volume}, "
                f"витрата палива на 100км: {self.fuel_efficiency_l_per_100km}")
    def __repr__(self):
        return {"make": self.make, "model": self.model, "year": self.model, "engine_volume": self.engine_volume,
                "fuel_efficiency_l_per_100km": self.fuel_efficiency_l_per_100km}
    def calculate_fuel_consumption(self, distance_km: int or float):
        return (self.fuel_efficiency_l_per_100km / 100) * distance_km

    @staticmethod
    def shift_gear(gear: str or int):
        print(f"Перемикаємо передачу на: {gear}")



if __name__ == '__main__':
    print("1:")
    print(Car("RangeRover", "Grande", 2015, 3.5, 0.3))
    dict1 = Car.__repr__(Car("RangeRover", "Grande", 2015, 3.5, 0.3))
    print(f"Словник: {dict1}")
    print(f"Витрата пального: {Car.calculate_fuel_consumption(Car("RangeRover", "Grande",
                                                2015, 3.5, 0.3),
                                            120)}")
    Car.shift_gear(1)
    Car.shift_gear(7)
    Car.shift_gear("N")

    print()
    print("2:")
    print(Car("Ferrari", "Kochernaya", 2025, 2.8, 0.4))
    dict2 = Car.__repr__(Car("Ferrari", "Kochernaya", 2025, 2.8, 0.4))
    print(f"Словник: {dict2}")
    print(f"Витрата пального: {Car.calculate_fuel_consumption(Car("Ferrari", "Kochernaya", 
                                                                  2025, 2.8, 0.4),
                                                              120)}")
    Car.shift_gear(2)
    Car.shift_gear(-1)
    Car.shift_gear("R")


