numbers = [15, 8, 22, 3, 45, 1, 30]

def porivnyannya(number):
    return number > 10

new_list = list(filter(porivnyannya, numbers))
print(new_list)


