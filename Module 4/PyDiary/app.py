from flask import Flask, render_template, redirect, url_for, flash, get_flashed_messages, session
from forms import LoginForm  # Імпортуємо наш клас форми

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sosage819qlkm2Or+Melembas_000oklqandqucunmebe845inskQ*' # Секретний ключ для сесій та CSRF-захисту

SESSION_TIMEOUT = 60 * 60 * 60

@app.post('/submit')
def submit_form():
    flash('Форму успішно відправлено!', 'success')
    return redirect(url_for('main_page'))


@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm() # Створюємо екземпляр форми
    if form.validate_on_submit():
        # Якщо форма відправлена і валідація пройшла успішно
        # Тут може бути ваша логіка входу (наприклад, перевірка пароля)
        return redirect(url_for('main_page'))
    
    # Якщо це GET-запит або валідація не пройшла,
    # відображаємо форму з помилками
    return render_template('login.html', form=form)

@app.get('/main')
def main_page():
    return render_template('main.html')

# form = LoginForm(): Створює об'єкт форми.
# form.validate_on_submit(): Цей метод робить дві речі:
#     1. Перевіряє, чи запит був POST і чи була натиснута кнопка відправки.
#     2. Виконує всі валідатори, визначені у класі форми. Якщо все добре, повертає True.
if __name__ == '__main__':
    app.run(debug=True, port=5084)