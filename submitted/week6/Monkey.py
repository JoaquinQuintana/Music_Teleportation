#to import environment run . environment.sh sets the app name and environment for flask. 

from flask import Flask, render_template, url_for
from markupsafe import escape


app = Flask(__name__) 

@app.route('/')

#use render template to call 
def index():
    return render_template('index.html')


@app.route('/You_Did_it')
def Monkeysite():
    return render_template('You_did_it.html')


#add additional route
@app.route('/contact')
def contact():
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
    
if __name__ == "__main__":
    app.run(debug=True)