cars = []

print('*' * 10, 'Гараж v.0.0.1', '*' * 10)

responce = 1
while responce:
  print("""Выбериет действие:
        1 - Добавить авто
        2 - Удалить авто
        3 - Вывести список
        4 - Поиск
        5 - Сортировка гаража
        0 - Выход""")
  responce = int(input("... "))
  if responce == 1:
    car = input("Новое авто: ")
    cars.append(car)
  elif responce == 2:
    car = input("Удалить авто: ")
    cars.remove(car)
  elif responce == 3:
    print(f'Всего машин в гараже {len(cars)} автомобилей \n{cars}')
  elif responce == 4:
    car = input("Поиск: ")
    if car in cars:
      print("Такая машина есть в гараже!")
    else:
      print("Такой машины нет в гараже!!!")
  elif responce == 5:
    cars.sort()
    print('Отсортировано!')
  else:
    print('Пока!')