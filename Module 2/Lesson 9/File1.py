# Це наш декоратор
def my_decorator(original_function):
    # Це внутрішня функція-"обгортка", яка містить додаткову логіку
    def wrapper_function():
        # Додаткова логіка ПЕРЕД викликом оригінальної функції
        print("Щось відбувається перед викликом функції.")

        # Виклик оригінальної функції
        original_function()

        # Додаткова логіка ПІСЛЯ виклику оригінальної функції
        print("Щось відбувається після виклику функції.")

    # Декоратор повертає нову, обгорнуту функцію
    return wrapper_function


@my_decorator
def say_hello():
    print("Привіт, світ!")

# Традиційний спосіб застосування декоратора
# decorated_hello = my_decorator(say_hello)
# decorated_hello()


# Тепер, коли ми викликаємо say_hello(), ми насправді викликаємо wrapper_function()
say_hello()









def log_arguments(func):
    def wrapper(*args, **kwargs):
        print(f"Викликається функція '{func.__name__}' з аргументами:")
        print(f"  Позиційні: {args}")
        print(f"  Іменовані: {kwargs}")
        result = func(*args, **kwargs)
        print("Функція завершила роботу.")
        return result

    return wrapper


@log_arguments
def add_numbers(a, b):
    return a + b


@log_arguments
def say_phrase(phrase, times=1):
    print(phrase * times)


result = add_numbers(5, 10)
print(f"Результат додавання: {result}")

say_phrase("Привіт! ", times=3)








# import time
#
#
# def timer(func):
#     """
#     Декоратор, що вимірює час виконання функції.
#     """
#
#     def wrapper(*args, **kwargs):
#         # 1. Записуємо час до виконання функції
#         start_time = time.time()
#
#         # 2. Викликаємо оригінальну функцію з усіма її аргументами
#         result = func(*args, **kwargs)
#
#         # 3. Записуємо час після виконання функції
#         end_time = time.time()
#
#         # 4. Обчислюємо та виводимо час виконання
#         execution_time = end_time - start_time
#         print(f"Функція '{func.__name__}' виконана за {execution_time:.4f} секунд.")
#
#         # 5. Повертаємо результат оригінальної функції
#         return result
#
#     return wrapper
#
#
# @timer
# def calculate_sum(n):
#     """Обчислює суму чисел від 0 до n."""
#     total = 0
#     for i in range(n):
#         total += i
#     return total
#
#
# @timer
# def power_of_numbers(numbers):
#     """Підносить кожне число у списку до другого степеня."""
#     return [num ** 2 for num in numbers]
#
#
# # --- Демонстрація роботи декоратора ---
#
# # Застосовуємо декоратор до функції, що виконує тривале обчислення
# sum_result = calculate_sum(10000000)
# print(f"Результат суми: {sum_result}\n")
#
# # Застосовуємо декоратор до функції, що працює зі списком
# numbers_list = list(range(1000000))
# squared_numbers = power_of_numbers(numbers_list)
# print("Довжина списку з квадратами чисел:", len(squared_numbers))