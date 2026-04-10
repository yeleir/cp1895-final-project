from flask import Flask, render_template, request, session, flash
from flask_session import Session

app = Flask(__name__)

app.secret_key = "super_secret_ps2_key"

app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = "filesystem"
Session(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/games')
def display_games():
    return render_template('games.html')

@app.route('/add')
def add_game():
    return render_template('add.html')

@app.route('/remove')
def remove_game():
    return render_template('remove.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)