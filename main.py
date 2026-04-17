from flask import Flask, render_template, request, session, flash
from flask_session import Session
import os

app = Flask(__name__)

app.secret_key = "super_secret_ps2_key"

app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = "filesystem"
Session(app)

save_location = "static/images"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/games')
def display_games():
    vault_data = session.get("games", {})
    return render_template('games.html', vault=vault_data)

@app.route('/add', methods=['GET', 'POST'])
def add_game():
    if request.method == 'POST':
        title = request.form['title']
        genre = request.form['genre']
        rating = request.form['rating']
        review = request.form['review']
        image_file = request.files['image']

        if image_file.filename != '':
            save_file_name = os.path.join(save_location, image_file.filename)
            image_file.save(save_file_name)

        if "games" in session:
            session["games"][title] = {'genre': genre, 'rating': rating, 'review': review, 'image': image_file.filename}
        else:
            session["games"] = {}
            session["games"][title] = {'genre': genre, 'rating': rating, 'review': review, 'image': image_file.filename}

        flash(f"'{title}' added to the vault!")
        return render_template('add.html')

    return render_template('add.html')

@app.route('/remove', methods=['GET', 'POST'])
def remove_game():
    vault = session.get("games", {})

    if request.method == 'POST':
        title_to_remove = request.form['title']

        if "games" in session and title_to_remove in session["games"]:
            session["games"].pop(title_to_remove)
            flash(f"'{title_to_remove}' was successfully removed!")

        return render_template('remove.html', vault=session.get("games", {}))
    return render_template('remove.html', vault=vault)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)