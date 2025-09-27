first_names = ["Іван", "Марія", "Олександр"]
last_names = ["Петров", "Іванова", "Коваль"]

def prices_operated(name, surname):
    return f"{name} {surname}"


new_list = list(map(prices_operated, first_names, last_names))
print(new_list)