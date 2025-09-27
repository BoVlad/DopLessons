import time


def func_timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Функція: {func.__name__}\n"
              f"Час виконання: {execution_time:.4f} секунд.")
        return result
    return wrapper

@func_timer
def calculate_sum(n: int):
    digit_sum = 0
    for i in range(0, n):
        digit_sum = digit_sum + i
    return digit_sum

@func_timer
def power_of_numbers(numbers: list):
    new_list = []
    for i in numbers:
        new_list.append(i ** 2)
    return new_list

def1 = calculate_sum(10000000)

big_list = list(range(1, 2000001))
def2 = power_of_numbers(big_list)

