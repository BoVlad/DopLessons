products = [('Яблуко', 2.5), ('Банан', 1.8), ('Апельсин', 3.0)]

there_no_func = lambda obj_list: sorted(obj_list, key=lambda obj: obj[1])

print(there_no_func(products))