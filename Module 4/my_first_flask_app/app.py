# from flask import Flask

# # 1. Створюємо екземпляр класу Flask
# app = Flask(__name__)

# # 2. Використовуємо @app.get() для обробки GET-запитів до головної сторінки ('/')
# @app.get('/')
# def hello_world():
#     # 3. Повертаємо повний HTML-документ
#     return '''
# <!doctype html>
# <html lang="uk">
# <head>
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Hello, Flask!</title>
#     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
# </head>
# <body>

#     <div class="container text-center mt-5">
#         <h1 class="display-4 text-primary">Привіт, це Flask з Bootstrap!</h1>
#         <p class="lead">Це наш перший веб-додаток, що повертає стилізований HTML.</p>
#     </div>

#     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
# </body>
# </html>
# '''

# # 4. Запуск сервера
# if __name__ == '__main__':
#     app.run(debug=True)















from flask import *

users = {"test@gmail.com": "qwerty123"}



app = Flask(__name__)

# Цей маршрут обробляє GET-запити до /about
@app.get('/about')
def about_page():
    return '''
<!doctype html>
<html lang="uk">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Про нас</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container text-center mt-5">
        <h1 class="display-4">Це сторінка "Про нас"</h1>
        <p class="lead">Це простий приклад GET-запиту.</p>
    </div>
</body>
</html>
'''


# Ця функція буде обробляти GET-запити до /login (відображення форми)
@app.get('/login')
def show_login_form():
    return '''
<!doctype html>
<html lang="uk">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Вхід</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center">Сторінка входу</h1>

        <form method="POST" action="/login">
            <div class="mb-3">
                <label for="email" class="form-label">Електронна пошта</label>
                <input type="email" class="form-control" id="email" name="email">
            </div>
            <div class="mb-3">
                <label for="password" class="form-label">Пароль</label>
                <input type="password" class="form-control" id="password" name="password">
            </div>
            <button type="submit" class="btn btn-primary">Увійти</button>
        </form>
    </div>
</body>
</html>
'''


# Ця функція буде обробляти POST-запити до /login (обробка даних)
@app.post('/login')
def login_user():
    # Отримуємо дані з форми за допомогою request.form
    email = request.form.get('email')
    password = request.form.get('password')
    if email in users and users.get(email) == password:
        return f'''
    <h1>Дані отримано!</h1>
    <p>Ваш email: {email}</p>
    <p>Ваш пароль: {password}</p>
    '''
    else:
        return redirect(url_for('about_page')) # Это немножко подсмотрел :)
    


if __name__ == '__main__':
    app.run(debug=True)