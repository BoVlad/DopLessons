class Vehicle:
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model  # Інкапсуляція: використовуємо _speed, щоб показати, що це внутрішній атрибут
        self._speed = 0


    # Гетер: Метод для отримання значення інкапсульованого атрибута
    @property
    def speed(self) -> int:
        """Повертає поточну швидкість транспортного засобу."""
        return self._speed


    # Сетер: Метод для зміни значення інкапсульованого атрибута
    @speed.setter
    def speed(self, new_speed: int):
        """Встановлює нову швидкість, перевіряючи її значення."""
        if new_speed >= 0:
            self._speed = new_speed
        else:
            print("Швидкість не може бути від'ємною!")


    def drive(self):
        """
        Загальний метод водіння.
        Буде перевизначений у дочірніх класах (поліморфізм).
        """
        print(f"{self.make} {self.model} рухається зі швидкістю {self.speed} км/год.")


    def __str__(self):
        return f"{self.make} {self.model}"



class Car(Vehicle):
    def __init__(self, make: str, model: str, num_doors: int): # Виклик конструктора батьківського класу за допомогою super()
        super().__init__(make, model)
        self.num_doors = num_doors
        self.honk_sound = "Біп-біп!"
    # Перевизначення методу drive з батьківського класу (Поліморфізм)
    def drive(self):
        """
        Специфічна для автомобіля реалізація методу drive.
        """
        print(f"{self.make} {self.model} з {self.num_doors} дверима їде плавно.")
        print(f"Поточна швидкість: {self.speed} км/год.")

    def honk(self):
        """Унікальний для класу Car метод."""
        print(f"{self.make} {self.model} сигналить: {self.honk_sound}")


if __name__ == "__main__":
    print("--- Демонстрація Інкапсуляції, Гетерів і Сетерів ---")
    my_vehicle = Vehicle("Boeing", "747")
    print(f"Початкова швидкість: {my_vehicle.speed} км/год.")

    my_vehicle.speed = 800  # Використання сетера @speed.setter
    print(f"Нова швидкість: {my_vehicle.speed} км/год.")

    my_vehicle.speed = -100  # Спроба встановити недопустиме значення
    print(f"Швидкість після невдалої спроби: {my_vehicle.speed} км/год.")

    print("\n--- Демонстрація Наслідування та Поліморфізму ---")

    # Створення об'єктів з різними реалізаціями
    car = Car("Toyota", "Camry", 4)
    truck = Vehicle("Ford", "F-150")

    # Зберігаємо об'єкти в одному списку
    vehicles = [car, truck]

    # Виклик методів. Зверніть увагу, що drive() поводить себе по-різному
    # для Car та Vehicle, що і є поліморфізмом.
    for vehicle in vehicles:
        print(f"\nОб'єкт: {vehicle}")
        # Встановлюємо швидкість, використовуючи метод батьківського класу
        vehicle.speed = 60
        vehicle.drive()  # Виклик методу, що демонструє поліморфізм

    print("\n--- Демонстрація унікального методу дочірнього класу ---")
    # Тільки об'єкт car має метод honk()
    car.honk()
    # truck.honk() # Цей виклик призведе до помилки, оскільки метод honk() не існує в класі Vehicle