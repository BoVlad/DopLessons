def celsius_to_fahrenheit(celsius):
    """Перетворює температуру з Цельсія у Фаренгейт."""
    return (celsius * 9/5) + 32

temperatures_c = [0, 10, 20, 30, 40]

# Використання map()
temperatures_f_map = map(celsius_to_fahrenheit, temperatures_c)

# Важливо! map() повертає ітератор, а не список.
# Щоб побачити результат, потрібно перетворити його на список:
result_list = list(temperatures_f_map)

print(result_list)
# Виведе: [32.0, 50.0, 68.0, 86.0, 104.0]

temperatures_f_loop = []
for temp in temperatures_c:
    temperatures_f_loop.append(celsius_to_fahrenheit(temp))

print(temperatures_f_loop)
# Результат такий самий, але код з map() коротший і більш "функціональний".