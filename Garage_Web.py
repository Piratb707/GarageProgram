from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    db = sqlite3.connect('garage.db')
    sql = db.cursor()
    cars = sql.execute("SELECT * FROM cars").fetchall()
    return render_template('index.html', cars=cars)

if __name__ == '__main__':
    app.run(debug=False)
