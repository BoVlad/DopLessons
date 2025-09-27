employees = [
    {'name': 'Іван', 'role': 'Manager', 'salary': 50000},
    {'name': 'Анна', 'role': 'Developer', 'salary': 60000},
    {'name': 'Марія', 'role': 'Manager', 'salary': 70000},
    {'name': 'Олег', 'role': 'Intern', 'salary': 20000}
]

def statusing(status):
    return status.get("role") == "Manager"

new_list = list(filter(statusing, employees))
print(new_list)