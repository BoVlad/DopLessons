str_numbers = ["10", "25", "50", "15"]

def str_to_int(string):
    if string.isdigit():
        return int(string)
    else:
        return None

new_list = list(map(str_to_int, str_numbers))
print(new_list)
