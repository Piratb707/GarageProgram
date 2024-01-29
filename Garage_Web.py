from flask import Flask, render_template
import sqlite3 as sql
import Main

app = Flask(__name__)

@app.route('/index')
def index():

    db = sql.connect(Main.name_db)
    cursor = db.cursor()
    list_cars = [i[0] for i in cursor.execute("SELECT * FROM cars").fetchall()]
    return render_template('index.html', name_db=Main.name_db, cars=list_cars)

@app.route('/')
def main():
    # TODO Create main page
    return render_template('main.html')

@app.route('/login')
def login():
    # TODO Create login page
    return render_template('login.html')

@app.route('/logout')
def logout():
    # TODO Create logout page
    return render_template('logout.html')

@app.route('/account')
def account():
    # TODO Create account page
    return "This is for account page"


if __name__ == '__main__':
    app.run(debug=False)