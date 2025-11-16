from flask import Flask, render_template, redirect, url_for, flash, get_flashed_messages
from forms import LoginForm  # Імпортуємо наш клас форми

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key' # Секретний ключ для сесій та CSRF-захисту



@app.get('/')
def index():
    # Відображаємо сторінку з повідомленнями
    return render_template('index.html')

@app.post('/submit')
def submit_form():
    # Тут може бути логіка обробки форми
    # ...
    # Відправляємо повідомлення про успіх
    flash('Форму успішно відправлено!', 'success')
    # Перенаправляємо користувача
    return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm() # Створюємо екземпляр форми

    if form.validate_on_submit():
        # Якщо форма відправлена і валідація пройшла успішно
        # Тут може бути ваша логіка входу (наприклад, перевірка пароля)
        return redirect(url_for('success_page')) # Перенаправлення на сторінку успіху
    
    # Якщо це GET-запит або валідація не пройшла,
    # відображаємо форму з помилками
    return render_template('login.html', form=form)

@app.route('/success')
def success_page():
    return '<h1>Вхід успішно виконано!</h1>'

# form = LoginForm(): Створює об'єкт форми.
# form.validate_on_submit(): Цей метод робить дві речі:
#     1. Перевіряє, чи запит був POST і чи була натиснута кнопка відправки.
#     2. Виконує всі валідатори, визначені у класі форми. Якщо все добре, повертає True.
if __name__ == '__main__':
    app.run(debug=True)