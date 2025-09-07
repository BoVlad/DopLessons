# 🧪 Міні-проєкт: Текстовий To-Do / Записник
# 🎯 Мета:
# Користувач додає та переглядає нотатки
# Дані зберігаються у файлі (.txt або .json)
#
# ✅ Що тренує цей проєкт:
# Роботу з файлами (.txt, .json)
# Менеджер with
# Серіалізацію JSON
# Прості функції
# Перевірку на помилки (try-except)


try:
    with open("data.txt", "r", encoding="utf-8") as file:
        filestart = file.readlines()
except FileNotFoundError:
    with open("data.txt", "w", encoding="utf-8") as file:
        pass


while True:
    print("1 - додати нотатку\n"
          "2 - показити всі нотатки\n"
          "3 - видалити нотатку\n"
          "4 - видалити всі нотатки\n")
    choice = input("Введіть вибір: ")
    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            new_notate = input("Введіть нотатку: ")
            with open("data.txt", "a", encoding="utf-8") as file:
                file.write(f"{new_notate}\n")
            print("Нотатка успішно додана!")
        elif choice == 2:
            index = 1
            with open("data.txt", "r", encoding="utf-8") as file:
                lines = file.readlines()
            for i in lines:
                print(f"{index}. {lines[index - 1].replace("\n", "")}")
                index = index + 1
            print()
        elif choice == 3:
            index = 1
            with open("data.txt", "r", encoding="utf-8") as file:
                lines = file.readlines()
            for i in lines:
                print(f"{index}. {lines[index - 1].replace("\n", "")}")
                index = index + 1
            delete_choice = input("Введіть номер нотатки для видалення: ")
            if delete_choice.isdigit():
                delete_choice = int(delete_choice)
                if 0 < delete_choice <= len(lines):
                    delete_choice = delete_choice - 1
                    del lines[delete_choice]
                    tempindex = 0
                    tempindex2 = 0
                    for i in lines:
                        if tempindex >= delete_choice and tempindex < (len(lines) - 1):
                            tempindex2 = tempindex + 1
                            lines[tempindex] = lines[tempindex2]
                            tempindex = tempindex + 1
                    with open("data.txt", "w", encoding="utf-8") as file:
                        file.writelines(lines)
                    print("Нотатка успішно видалена")
                else:
                    print("Нотатки з таким номером немає")
            else:
                print("Ви не ввели цифру")
        elif choice == 4:
            with open("data.txt", "w", encoding="utf-8") as file:
                file.write("")
            print("Всі нотатки успішно видалені")
        else:
            print("Такого пункта в меню немає")
    else:
        print("Ви не ввели цифру")