from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.environ['MYSQL_USER']}:{os.environ['MYSQL_PASSWORD']}@{os.environ['MYSQL_HOST']}:{os.environ['MYSQL_PORT']}/{os.environ['MYSQL_DB']}"
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)

USERNAME = 'admin'
PASSWORD = 'password'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USERNAME and password == PASSWORD:
            return redirect('/dashboard')
        else:
            return render_template('index.html', message='Invalid credentials')
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return 'Welcome to the dashboard'

if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', port=5000)
