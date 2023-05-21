from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Define the username and password
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
    app.run(host='0.0.0.0', port=80)
