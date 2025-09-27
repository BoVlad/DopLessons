# Завдання 5: Симуляція ферми
# Ціль: Застосувати принципи успадкування та поліморфізм для створення повноцінної
# симуляції ферми.
#
# Частина 1: Базовий клас Animal
# Створіть базовий клас Animal. Цей клас буде представляти спільні характеристики
# для всіх тварин на фермі.
#
# Атрибути: name та sound.
#
# Методи: __init__, make_sound(self) та __str__.
#
# Частина 2: Дочірні класи
# Створіть декілька класів: Cow, Sheep, Chicken, які успадковують від Animal.
#
# Кожен клас повинен надавати власну реалізацію для звуку.
#
# Використовуйте super() для виклику конструктора батьківського класу.
#
# Частина 3: Поліморфізм в дії
# Додайте до базового класу Animal метод feed(self, food), який просто виводить,
#  що тварина їсть.
#
# У класі Chicken перевизначте метод feed. Нехай він виводить, що курка їсть,
# а також додає повідомлення '...і знесла яйце!'.

class Animal:
    def __init__(self, name: str, sound: str):
        self.name = name
        self.sound = sound
    def __str__(self):
        return (f"Ім'я тварини: {self.name},\n"
                f"Видає звук: {self.sound}")
    def make_sound(self):
        print(f"Звук '{self.sound}' від {self.name}")
    def feed(self, feed):
        print(f"{self.name} їсть {feed}")


class Cow(Animal):
    def __init__(self, name: str, sound: str):
        super().__init__(name, sound)
    def make_sound(self):
        print(f"Протяжний звук '{self.sound}' від {self.name}")

class Sheep(Animal):
    def __init__(self, name: str, sound: str):
        super().__init__(name, sound)
    def make_sound(self):
        print(f"{self.name} бекає: '{self.sound}'")

class Chicken(Animal):
    def __init__(self, name: str, sound: str):
        super().__init__(name, sound)
    def make_sound(self):
        print(f"{self.name} потужно кричить: '{self.sound}'")
    def feed(self, feed):
        print(f"{self.name} їсть {feed}")
        print("...і знесла яйце!")







