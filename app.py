import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_contacts(contacts_id):
    conn = get_db_connection()
    contacts = conn.execute('SELECT * FROM contacts WHERE id = ?',
                        (contacts_id,)).fetchone()
    conn.close()
    if contacts is None:
        abort(404)
    return contacts

@app.route('/')
def index():
    conn = get_db_connection()
    contacts = conn.execute('SELECT * FROM contacts').fetchall()
    conn.close()
    return render_template('test.html', contacts=contacts)


@app.route('/<int:contacts_id>')
def post(contacts_id):
    contacts = get_contacts(contacts_id)
    return render_template('post.html', post=post)


@app.route('/contact', methods=('GET', 'POST'))
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        content = request.form['content']

        if not name:
            flash('Name is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO contacts (uname, email, content) VALUES (?, ?, ?)',
                         (name, email, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('contact.html')