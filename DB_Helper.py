import sqlite3


def create_db(path: str):
    """
    Создаем базу данных sqlite.
    :param path: Путь к базе данных.
    """
    connect = sqlite3.connect(path)
    cursor = connect.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cars(
            car TEXT
        )
    """)
    connect.commit()
    cursor.close()
    connect.close()


def vacuum_db(path: str):
    """
    Очистка пустых значений из базы.
    :param path: Путь к базе данных.
    """
    conn = sqlite3.connect(path)
    conn.execute("VACUUM")
    conn.close()


def open_db(path: str) -> list:
    """
    Получение данных из базы Из таблицы _cars_
    :param path: Путь к базе данных.
    """
    connect = sqlite3.connect(path)
    cursor = connect.cursor()
    cursor.execute(f"SELECT car FROM cars")
    data = [i[0] for i in cursor.fetchall()]
    cursor.close()
    connect.close()
    return data


def insert_db(path: str, car: str):
    connect = sqlite3.connect(path)
    cursor = connect.cursor()
    cursor.execute(f"INSERT INTO cars VALUES ('{car}')")
    connect.commit()
    cursor.close()
    connect.close()


def delete_db(path: str, car: str):
    connect = sqlite3.connect(path)
    cursor = connect.cursor()
    cursor.execute(f"DELETE FROM cars WHERE car = '{car}'")
    connect.commit()
    cursor.close()
    connect.close()

