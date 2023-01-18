import sqlite3
import unittest

class TestGarage(unittest.TestCase):
    def setUp(self):
        self.db = sqlite3.connect('garage.db')
        self.sql = self.db.cursor()
        self.sql.execute("CREATE TABLE IF NOT EXISTS cars(car TEXT)")
        self.db.commit()

    def test_add_car(self):
        # Тест добавления
        car = "Chevrolet"
        self.sql.execute(f"INSERT INTO cars VALUES ('{car}')")
        self.db.commit()
        self.sql.execute(f"SELECT car FROM cars WHERE car = '{car}'")
        self.assertEqual(self.sql.fetchone()[0], car)

    def test_remove_car(self):
        # Тест удаления
        car = "Honda"
        self.sql.execute(f"INSERT INTO cars VALUES ('{car}')")
        self.db.commit()
        self.sql.execute(f"SELECT car FROM cars WHERE car = '{car}'")
        self.assertEqual(self.sql.fetchone()[0], car)
        self.sql.execute(f"DELETE FROM cars WHERE car = '{car}'")
        self.db.commit()
        self.sql.execute(f"SELECT car FROM cars WHERE car = '{car}'")
        self.assertIsNone(self.sql.fetchone())

    def test_list_cars(self):
        # Тест списка
        cars = ["Nissan", "Mazda", "Ford"]
        for car in cars:
            self.sql.execute(f"INSERT INTO cars VALUES ('{car}')")
            self.db.commit()
        self.sql.execute("SELECT * FROM cars")
        self.assertEqual([i[0] for i in self.sql.fetchall()], cars)

    def tearDown(self):
        self.sql.execute("DROP TABLE cars")
        self.db.commit()
        self.db.close()

if __name__ == '__main__':
    unittest.main()