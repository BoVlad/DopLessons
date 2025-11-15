from flask import *

app = Flask(__name__)


# Маршрут для списку постів
@app.get('/contact')
def contact_form():
    return render_template("contact_form.html")

@app.post('/submit_feedback')
def submit_feedback_form():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    return jsonify([name, email, message])

if __name__ == '__main__':
    app.run(debug=True)