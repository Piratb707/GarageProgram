import DB_Helper as db


def menu():
    print("""Выберите действие:
            1 - Добавить авто
            2 - Удалить авто
            3 - Вывести список
            4 - Поиск
            0 - Выход""")
    while 1:
        result = int(input("... "))
        if (result >= 0) and (result <= 4):
            return result
        else:
            print("Введите корректное число [1..4, 0]")


version = '1.0.1'
print('Garage', version)

name_db = "garage.db"
db.create_db(name_db)

response = 1

while response:
    response = menu()
    if response == 1:
        car = input("Новое авто: ")
        list_cars = db.open_db(name_db)
        if car in list_cars:
            print(f"Автомобиль {car} у вас уже есть!")
        else:
            db.insert_db(name_db, car)
            print("Добавлено!")

    elif response == 2:
        car = input("Удалить авто: ")
        list_cars = db.open_db(name_db)
        if car not in list_cars:
            print(f"У вас нет автомобиля {car}")
        else:
            db.delete_db(name_db, car)
            print("Запись удалена...")

    elif response == 3:
        list_cars = db.open_db(name_db)
        for car in list_cars:
            print(car)

    elif response == 4:
        car = input("Поиск: ")
        list_cars = db.open_db(name_db)
        if car in list_cars:
            print(f"Автомобиль {car} есть у вас в гараже!")
        else:
            print(f"Автомобиль {car} отсутствует в вашем гараже!")

    else:
        print('Пока!')
