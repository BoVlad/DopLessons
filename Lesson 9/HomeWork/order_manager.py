import json
import pytest

try:
    with open("db/orders.json", "r", encoding="utf-8") as file:
        pass
except FileNotFoundError:
    with open("db/orders.json", "w", encoding="utf-8") as file:
        pass


def load_data():
    try:
        with open("db/orders.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return False

def save_data(data):
    with open("db/orders.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return True


def new_order(name, product, quantity):
    new_data = load_data()
    try:
        new_data[name][product] = quantity
    except Exception:
        new_data[name] = {}
        new_data[name][product] = quantity
    save_data(new_data)
    print("Замовлення підтверджено!")
    return True

if __name__ == "__main__":
    name = input("Введіть ваше ім'я: ")

    while True:
        print(f"Привіт, {name}!")
        product = input("Введіть назву того, що ви хочете замовити: ")
        quantity = input("Введіть кількість (тільки цілі цифри): ")
        if quantity.isdigit():
            quantity = int(quantity)
            if quantity <= 0:
                print("Невірна кількість")
                continue
            else:
                pass
        else:
            print("Невірна кількість")
            continue
        new_order(name=name, product=product, quantity=quantity)



