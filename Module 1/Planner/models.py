class Notate:
    def __init__(self, id: int, title: str, deadline: str, done: bool = False):
        self.dict = {"id": id,
                     "title": title,
                     "deadline": deadline,
                     "done": done}


menu = """Команди:

add - додати нове завдання
list - переглянути всі завдання
done - відмітити як виконане
delete - видалити завдання
exit - завершити роботу"""