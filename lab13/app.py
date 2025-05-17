"""
Sally Han
lab13, Flask application
"""
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

""" create an object 'app' from the Flask module.
    __name__ set to __main__ if the script is running directly from the main file
"""
app = Flask(__name__)

# connecting to Postgresql
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:hrs7453377@localhost/demoDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #  False set to avoid warning messages, save memory.

# create an object db
db = SQLAlchemy(app)

# definea model (create table in the 'demoDB' database)
class UserLogin(db.Model):
    id = db.Column(db.Integer, primary_key = True) # primary key
    username = db.Column(db.String(80), nullable = False)# username column

# set the routing to the main page
# 'route' decorator is used to access the root URL
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
       return 'Successfully requested! Entered password =' + request.form['password'] # if submission went through successfully.
    name = "Sally"
    checkfruit = "pineapple"
    fruits = ['apple', 'orange', 'grapes']
    return render_template('index.html', username=name, listfruits = fruits, checkfruit=checkfruit)
                   
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/users')
def users():
    return render_template('users.html')

@app.route('/quotes')
def quotes():
    return redirect(url_for('index'))

# set the 'app' to run if you execute the file directly(not when it is imported)
if __name__ == '__main__':
    with  app.app_context(): db.create_all()
    app.run(debug = True)


