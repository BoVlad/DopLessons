# Звичайна функція
def add_numbers(x, y):
    return x + y

print(add_numbers(5, 3)) # Виведе: 8

# Lambda-функція, яка робить те саме
add_lambda = lambda x, y: x + y

print(add_lambda(5, 3)) # Виведе: 8
# Як бачите, lambda дозволяє створити функцію в одному рядку.

# 3. Основні випадки використання
# Хоча lambda-функції можна присвоювати змінним, їх головна сила проявляється, коли вони використовуються як аргументи для інших функцій.

# З map(): Робить код дуже лаконічним.

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)
# Виведе: [1, 4, 9, 16, 25]
# З filter(): Дозволяє задати умову фільтрації прямо в одному рядку.

scores = [85, 92, 78, 95, 60]
high_scores = list(filter(lambda score: score >= 90, scores))
print(high_scores)
# Виведе: [92, 95]
# З sorted(): Це один із найпоширеніших і корисних сценаріїв. lambda дозволяє сортувати складні послідовності за певним ключем.

students = [
    {'name': 'Іван', 'age': 20},
    {'name': 'Марія', 'age': 22},
    {'name': 'Олег', 'age': 19}
]

# Сортування за віком
sorted_by_age = sorted(students, key=lambda student: student['age'])
print(sorted_by_age)
# Виведе: [{'name': 'Олег', 'age': 19}, {'name': 'Іван', 'age': 20}, {'name': 'Марія', 'age': 22}]