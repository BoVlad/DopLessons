from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Імітація бази даних (список словників)
notes = [
    {'id': 1, 'title': 'Перша нотатка', 'content': 'Це моя перша нотатка.'},
    {'id': 2, 'title': 'Плани на тиждень', 'content': 'Вивчити Flask, створити CRUD.'}
]
# Лічильник для унікальних ID
next_id = 3
# --- GET-запити (Read) ---

# Маршрут для головної сторінки (список нотаток)
@app.get('/')
def index():
    return render_template('index.html', notes=notes)

# Маршрут для перегляду однієї нотатки
@app.get('/note/<int:note_id>')
def view_note(note_id):
    # Знайдіть нотатку за ID
    note = next((n for n in notes if n['id'] == note_id), None)
    if note is None:
        return "Нотатка не знайдена", 404
    return render_template('view_note.html', note=note)

# Маршрут для форми додавання
@app.get('/add')
def add_note_form():
    return render_template('add_note.html')

# Маршрут для форми редагування
@app.get('/edit/<int:note_id>')
def edit_note_form(note_id):
    note = next((n for n in notes if n['id'] == note_id), None)
    if note is None:
        return "Нотатка не знайдена", 404
    return render_template('edit_note.html', note=note)

# --- POST-запити (Create, Update, Delete) ---

# Маршрут для створення нотатки
@app.post('/add')
def add_note():
    global next_id
    title = request.form.get('title')
    content = request.form.get('content')
    
    new_note = {'id': next_id, 'title': title, 'content': content}
    notes.append(new_note)
    next_id += 1
    
    # Після додавання перенаправляємо на головну сторінку
    return redirect(url_for('index'))

# Маршрут для оновлення нотатки
@app.post('/edit/<int:note_id>')
def edit_note(note_id):
    note = next((n for n in notes if n['id'] == note_id), None)
    if note is None:
        return "Нотатка не знайдена", 404
    
    note['title'] = request.form.get('title')
    note['content'] = request.form.get('content')
    
    return redirect(url_for('index'))

# Маршрут для видалення нотатки
@app.post('/delete/<int:note_id>')
def delete_note(note_id):
    global notes
    notes = [n for n in notes if n['id'] != note_id]
    
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)