import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO contacts (uname, email, content) VALUES (?, ?, ?)",
            ('Test First Name', 'first@gmail', 'Test content for the first name')
            )

cur.execute("INSERT INTO contacts (uname, email, content) VALUES (?, ?, ?)",
            ('Test Second Name', 'second@gmail','Test content for the second name')
            )

connection.commit()
connection.close()