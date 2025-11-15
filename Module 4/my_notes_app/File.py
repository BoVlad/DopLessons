# У Flask ви можете працювати з куками безпосередньо за допомогою об'єкта request.cookies (для читання) та response.set_cookie() (для запису).

# 3. Використання Sessions у Flask
# Для роботи з сесіями вам потрібно виконати два кроки:

# Встановити секретний ключ. Це критично важливо для безпеки. Додайте рядок app.secret_key = 'ваш_дуже_складний_секретний_ключ' у ваш файл app.py.

# Імпортувати об'єкт session з Flask. Цей об'єкт поводиться як словник, і ви можете додавати, змінювати або видаляти дані.



# # app.py

# from flask import Flask, session, request

# app = Flask(__name__)

# # ЦЕ ОБОВ'ЯЗКОВО! Встановіть надійний ключ.
# app.secret_key = 'very_secret_and_complex_key_12345'

# # Збереження даних у сесію
# session['username'] = 'user123'

# # Отримання даних з сесії
# username = session.get('username') # використання .get() безпечніше, ніж ['username']

# # Видалення даних
# session.pop('username', None) # .pop() видаляє елемент
# session.clear() # Видаляє всі дані з сесії