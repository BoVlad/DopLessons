from file_utils import program_start, load_data, save_data
from models import Notate, menu

program_start()


message = ""

print("Привіт, це твій консольний помічник з додаток!")

print(type(load_data()))

while True:
    print(menu)
    print()
    choose = input("Введіть ваш вибір: ")
    if not choose.isdigit():
        choose = choose.strip().lower()
        if choose == "add":
            title = input("Введіть саме завдання: ")
            if title.strip() == "" or title.isdigit():
                print("Завдання не може бути пусте, або не може бути лише цифрою!")
                print()
                continue
            deadline = input("Введіть дедлайн (рік-місяць-число): ")
            data = load_data()
            now_id = data.get("now_id") + 1
            note = Notate(id=now_id, title=title, deadline=deadline, done=False)
            data["tasks"].append(note.dict)
            data["now_id"] = now_id
            save_data(data=data)
            print("Дані успішно додані!")
            print()
        elif choose == "list":
            data = load_data()
            for i in data["tasks"]:
                print(f"ID: {i["id"]}")
                print(f"Завдання: {i["title"]}")
                print(f"Дедлайн: {i["deadline"]}")
                if i["done"]:
                    print("Зроблено: Так")
                else:
                    print("Зроблено: Ні")
                print()
            print()
            print()
        elif choose == "done":
            id_number = input("Введіть ID завдання: ")
            if id_number.isdigit():
                id_number = int(id_number)
                data = load_data()
                for i in range(0, len(data["tasks"])):
                    if data["tasks"][i]["id"] == id_number:
                        data["tasks"][i]["done"] = True
                        save_data(data=data)
                        message = "Дані успішно редаговано!"
                        break
                    else:
                        message = "Не вдалося знайти завдання за таким ID!"
                print(message)
                print()
            else:
                print("Ви не ввели цифру!")
                print()
                continue
        elif choose == "delete":
            id_number = input("Введіть ID завдання: ")
            if id_number.isdigit():
                id_number = int(id_number)
                data = load_data()
                for i in range(0, len(data["tasks"])):
                    if data["tasks"][i]["id"] == id_number:
                        del data["tasks"][i]
                        save_data(data=data)
                        message = "Завдання успішно видалено!"
                        break
                    else:
                        message = "Не вдалося знайти й видалити завдання за таким ID!"
                print(message)
                print()
            else:
                print("Ви не ввели цифру!")
                print()
                continue
        elif choose == "exit":
            print("Завершення роботи...")
            break
        else:
            print("Такої команди немає!")
            print()
    else:
        print("Ви ввели цифру, а не команду!")
        print()

