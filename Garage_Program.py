import sqlite3

print('Garage 1.0')

db = sqlite3.connect('garage.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS cars(
    car TEXT
)
""")
db.commit()

responce = 1

while responce:
  print("""Выбериет действие:
        1 - Добавить авто
        2 - Удалить авто
        3 - Вывести список
        4 - Поиск
        0 - Выход""")
  responce = int(input("... "))
  if responce == 1:
    car = input("Новое авто: ")
    sql.execute(f"SELECT car FROM cars WHERE car = '{car}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO cars VALUES ('{car}')")
        db.commit()

        print("Добавлено!")
    else:
        print(f"Автомобиль {car} у вас уже есть!")

  elif responce == 2:
    car = input("Удалить авто: ")
    sql.execute(f"SELECT car FROM cars WHERE car = '{car}'")
    if sql.fetchone() is None:
        print(f"У вас нет автомобиля {car}")
    else:
        sql.execute(f"DELETE FROM cars WHERE car = '{car}'")
        db.commit()

  elif responce == 3:
    cars = sql.execute("SELECT * FROM cars")
    for i in cars:
        print(i)

  elif responce == 4:
    car = input("Поиск: ")
    sql.execute(f"SELECT * FROM cars WHERE car = '{car}'")
    if sql.fetchone() is None:
        print(f"Автомобиль {car} отсутствует в вашем гараже!")
    else:
        print(f"Автомобиль {car} есть у вас в гараже!")
  else:
    print('Пока!')