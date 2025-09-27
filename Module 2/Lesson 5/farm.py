# Частина 4: Симуляція
# Створіть основний файл farm.py, який буде містити всю логіку симуляції.
#
# Створіть об'єкти кожного з дочірніх класів.
#
# Зберіть усі об'єкти в один список, наприклад, animals = [cow, sheep, chicken].
#
# Використовуючи цикл for, пройдіться по списку animals та для кожного об'єкта
# викличте методи make_sound() та feed(). Зверніть увагу, як один і той же виклик
# make_sound() призводить до різних результатів завдяки поліморфізму.

from farm_OOP import (Cow, Sheep, Chicken)


print("Вітаємо на фермі!\n")

cow = Cow("Зіна", "Муууууу")
sheep = Sheep("Ліда", "Бе-е-е-е-е-е-е")
chicken = Chicken("Вікторія", "Кух-ку-дах")

animals = [cow, sheep, chicken]

for animal in animals:
    print(animal)
    animal.make_sound()
    animal.feed("Трава")
    print()
