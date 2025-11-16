from flask import *
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sos1so4ka4uZ*&Tg8#d0v!9v@zq3x'


@app.get('/contact')
def contact_form():
    form = LoginForm()
    return render_template("contact_form.html", form=form)

    
@app.post('/submit_feedback')
def submit_feedback_form():
    form = LoginForm()
    name = form.name.data
    email = form.email.data
    message = form.message.data
    # message = request.form.get('message')
    if not form.validate_on_submit():
        return jsonify({'errors': form.errors}), 400
    return jsonify({"name": name, "email": email, "message": message})

if __name__ == '__main__':
    app.run(debug=True)