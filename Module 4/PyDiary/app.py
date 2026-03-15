from flask import (
    Flask,
    render_template,
    redirect,
    url_for,
    flash,
    get_flashed_messages,
    session,
)
from forms import LoginForm  # Імпортуємо наш клас форми
from session_utilities import login_required, login_forbidden, user_in_session, get_user_role
from file_utils import program_start, is_user_in_db

program_start()

app = Flask(__name__)
app.config["SECRET_KEY"] = (
    "sosage819qlkm2Or+Melembas_000oklqandqucunmebe845inskQ*"  # Секретний ключ для сесій та CSRF-захисту
)

SESSION_TIMEOUT = 60 * 60 * 60
app.config["PERMANENT_SESSION_LIFETIME"] = SESSION_TIMEOUT

@app.get("/")
@login_required
def main_page():
    return render_template("main.html", user_role=get_user_role())

@app.post("/submit")
def submit_form():
    flash("Форму успішно відправлено!", "success")
    return redirect(url_for("main_page"))


@login_forbidden
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()  # Створюємо екземпляр форми
    if form.validate_on_submit():
        # Якщо форма відправлена і валідація пройшла успішно
        # Тут може бути ваша логіка входу (наприклад, перевірка пароля)
        return redirect(url_for("main_page"))

    # Якщо це GET-запит або валідація не пройшла,
    # відображаємо форму з помилками
    return render_template("login.html", form=form)



if __name__ == "__main__":
    app.run(debug=True, port=5084)
