import json

def program_start():
    try:
        with open("tasks.json", "r", encoding="utf-8"):
            pass
    except FileNotFoundError:
        data = {"now_id": 0, "tasks": []}
        with open("tasks.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


def load_data():
    try:
        with open("tasks.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(e)


def save_data(data):
    with open("tasks.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)