import json

try:
    with open("database.json", "r", encoding="utf-8"):
        pass
except FileNotFoundError:
    data = {}
    with open("database.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)



def load_data():
    try:
        with open("database.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(e)
        return None


def save_data(data):
    with open("database.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)



def find_first_unique_char(message: str):
    dict = {}
    return_message = None
    data = load_data()
    if message in data:
        return_message = data.get(message)
    else:
        for symbol in message:
            try:
                dict[symbol] = dict.get(symbol) + 1
            except Exception:
                dict[symbol] = 1
        for key in dict:
            if dict.get(key) == 1:
                return_message = key
                break
        data[message] = return_message
        save_data(data)
    return return_message


if __name__ == "__main__":
    message_to_def = input("Введіть строку для перевірки: ")
    print(f"Перший символ, який не повторюється: {find_first_unique_char(message_to_def)}")




