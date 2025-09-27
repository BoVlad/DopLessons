prices = [100, 250, 75, 420]

def prices_operated(price):
    return int(price * 0.8)


new_list = list(map(prices_operated, prices))
print(new_list)