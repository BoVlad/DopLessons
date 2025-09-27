def is_even(number):
    """Перевіряє, чи є число парним."""
    return number % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Використання filter()
even_numbers_filter = filter(is_even, numbers)

# Важливо! filter() повертає ітератор, а не список.
# Щоб побачити результат, потрібно перетворити його на список:
result_list = list(even_numbers_filter)

print(result_list)
# Виведе: [2, 4, 6, 8, 10]
# Для порівняння, та ж сама операція за допомогою циклу for:

even_numbers_loop = []
for number in numbers:
    if is_even(number):
        even_numbers_loop.append(number)

print(even_numbers_loop)
# Результат такий самий, але filter() дозволяє виразити намір (фільтрацію)
# більш лаконічно.
# 3. Корисний прийом: filter(None, iterable)
# Якщо ви хочете просто видалити всі "falsy" (хибні) значення зі списку (такі як None, 0, '', [], False), можна передати None як функцію.

mixed_list = [1, '', 'hello', 0, None, 'world', []]

# Залишиться все, що не є falsy
clean_list = list(filter(None, mixed_list))

print(clean_list)
# Виведе: [1, 'hello', 'world']