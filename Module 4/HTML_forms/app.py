from flask import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sos1so4ka4uZ*&Tg8#d0v!9v@zq3x'

# Маршрут для списку постів
@app.get('/contact')
def contact_form():
    return render_template("contact_form.html")
    # render_template: Функція для рендерингу HTML-шаблонів.
    
@app.post('/submit_feedback')
def submit_feedback_form():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    return jsonify([name, email, message])

if __name__ == '__main__':
    app.run(debug=True)