from flask import *

app = Flask(__name__)



# from flask import Flask, jsonify

# app = Flask(__name__)

# # Дані, які ми будемо повертати (імітація бази даних)
# products = [
#     {'id': 1, 'name': 'Laptop', 'price': 1200},
#     {'id': 2, 'name': 'Mouse', 'price': 25},
#     {'id': 3, 'name': 'Keyboard', 'price': 75}
# ]

# @app.get('/api/products')
# def get_products():
#     # Повертаємо список продуктів як JSON
#     return jsonify(products)
# 
# 
# 
# # app.py

# from flask import Flask, render_template

# app = Flask(__name__)

# @app.get('/hello')
# def render_hello():
#     name = "Олесь"
#     # Передаємо змінну name в шаблон hello.html
#     return render_template('hello.html', user_name=name)

# if __name__ == '__main__':
#     app.run(debug=True)

# Імітація даних, що зберігаються у базі даних
posts = [
    {'id': 1, 'title': 'Перший крок у Flask', 'author': 'Іван', 'content': 'Сьогодні ми вивчили, як...'},
    {'id': 2, 'title': 'Про що говорять декоратори', 'author': 'Марія', 'content': 'Декоратори - це потужний інструмент...'},
    {'id': 3, 'title': 'Основи роботи з шаблонами Jinja2', 'author': 'Петро', 'content': 'Jinja2 дозволяє зробити HTML-сторінки...'}
]

# Маршрут для списку постів
@app.get('/blog')
def show_blog_list():
    # Передаємо весь список постів у 
    # Ваш код
    try:
        return render_template("blog_list.html", posts=posts)
    except NameError as e:
        return render_template("blog_list.html", posts=[])

# Маршрут для детального перегляду одного посту
# <int:post_id> - це динамічна частина URL, яка очікує ціле число
@app.get('/blog/<int:post_id>')
def show_post_detail(post_id):
    # Шукаємо пост за його ID у списку
    # Ваш код
    post = next((p for p in posts if p['id'] == post_id), None) # Вы сами сказали что можна гуглить)
    if post is None:
        return "Пост не знайдено", 404
    return render_template("post_detail.html", post=post)
    # Передаємо знайдений пост у шаблон
    # Ваш код
    
# Маршрут для API (повертає JSON)
@app.get('/api/posts')
def get_posts_api():
    # Повертаємо список постів як JSON
    return jsonify(posts)

if __name__ == '__main__':
    app.run(debug=True)