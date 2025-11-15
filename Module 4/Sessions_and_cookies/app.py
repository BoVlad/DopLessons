# 1. Cookies (Куки)
# Cookies — це невеликі текстові файли, які сервер відправляє браузеру, а браузер зберігає на стороні клієнта. При кожному наступному запиті до того ж сервера, браузер автоматично відправляє ці куки назад.
# 
# Особливості:
# 
# Зберігаються на клієнті: Браузер зберігає їх локально.
# 
# Небезпечно зберігати конфіденційні дані: Куки можна переглянути, змінити або видалити, тому ніколи не зберігайте там паролі чи іншу чутливу інформацію.
# 
# Обмеження за розміром: Зазвичай до 4 КБ.
# 
# У Flask ви можете працювати з куками безпосередньо за допомогою об'єкта request.cookies (для читання) та response.set_cookie() (для запису)


# Sessions — це набагато безпечніший та ефективніший механізм для підтримання стану. У цьому випадку:
# 
# Дані зберігаються на сервері.
# 
# Клієнту відправляється лише ідентифікатор сесії (Session ID) у вигляді куки.
# 
# Коли браузер відправляє запит, він надсилає цей ID. Ваш Flask-додаток отримує ID, знаходить відповідні дані сесії на сервері та робить їх доступними.
# 
# Ключова перевага: Дані сесії криптографічно підписані за допомогою секретного ключа (SECRET_KEY), що гарантує їхню цілісність і захищає від підробки.
# 
# 3. Використання Sessions у Flask
# Для роботи з сесіями вам потрібно виконати два кроки:
# 
# Встановити секретний ключ. Це критично важливо для безпеки. Додайте рядок app.secret_key = 'ваш_дуже_складний_секретний_ключ' у ваш файл app.py.
# 
# Імпортувати об'єкт session з Flask. Цей об'єкт поводиться як словник, і ви можете додавати, змінювати або видаляти дані.

from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = "sosiska48A*liK2[op02}L/a"

# Маршрут для головної сторінки (список нотаток)
@app.get('/')
def index():
    return render_template('index.html')

@app.get('/login')
def login_form():
    return render_template('login.html')

@app.post('/login')
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == "user" and password == "pass":
        session['username'] = username
        responce = redirect(url_for('index'))
        now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        responce.set_cookie('last_login', now_time)
        return responce
    else:
        return "Невірні облікові дані", 401

@app.get('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

    