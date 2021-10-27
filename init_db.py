import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO contacts (uname, email, content) VALUES (?, ?)",
            ('First Name', 'first@gmail', 'Content for the first name')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Name', 'second@gmail','Content for the second name')
            )

connection.commit()
connection.close()