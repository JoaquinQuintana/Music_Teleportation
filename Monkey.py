#to import environment run . environment.sh sets the app name and environment for flask. 

from flask import Flask, render_template, url_for,request
from markupsafe import escape
import re

def HTML_editor(HTMLfileName):
    fileName = "templates/" + HTMLfileName
    reading_file = open(fileName,"r")

    new_file_content = ""
    for line in reading_file:
        stripped_line = line.strip()
        new_line = stripped_line.replace("George", "Joaquin")
        new_file_content += new_line +"\n"
    reading_file.close()

    writing_file = open(fileName, "w")
    writing_file.write(new_file_content)
    writing_file.close()

    return

app = Flask(__name__) 

@app.route('/')

#use render template to call 
def index():
    return render_template('index.html')


@app.route('/You_Did_it')
def Monkeysite():
    return render_template('You_did_it.html')


#add additional route
@app.route('/contact', methods =["GET", "POST"])
def contact():
    if request.method == "POST":
        # getting input with name = fname in HTML form
        mood = request.form.get("moods")
        # getting input with name = lname in HTML form
        #last_name = request.form.get("lname")
        return "Mood Selected " + mood
    return render_template('contact.html')


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)


#print out the urls for the functions 
with app.test_request_context():
    print('URL for index: ',url_for('index'))
    print('URL for contact: ',url_for('contact'))
    print(url_for('Monkeysite'))
    print(url_for('show_user_profile', username = 'George'))
    #HTML_editor('index.html')
    
if __name__ == "__main__":
    app.run(debug=True)