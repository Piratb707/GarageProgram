from flask import Flask, render_template
import sqlite3 as sql
import Main

app = Flask(__name__)



@app.route('/')
def index():

    db = sql.connect(Main.name_db)
    cursor = db.cursor()
    list_cars = [i[0] for i in cursor.execute("SELECT * FROM cars").fetchall()]
    return render_template('index.html', name_db=Main.name_db, cars=list_cars)

if __name__ == '__main__':
    app.run(debug=False)
