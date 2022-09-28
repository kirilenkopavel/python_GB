"""
Задача 3. Напишите программу, которая принимает на вход координаты точки (X и Y), при этом X ≠ 0 и Y ≠ 0 и выдаёт номер
четверти плоскости, в которой находится эта точка (или на какой оси она находится).
"""


def taking_coordinates():
    # принимает вводимые координаты
    try:
        x = float(input("Введите координату Х: "))
        y = float(input("Введите координату Y: "))
        if x == 0 or y == 0:
            print("Координаты не могут быть 0!")
            taking_coordinates()
        coordinates = [x, y]
        return coordinates
    except Exception:
        print("Необходимо вводить цифры")
        taking_coordinates()


def find_coordinate_point(coordinates):
    # определяем какой четверти принадлежит точка
    x = coordinates[0]
    y = coordinates[1]
    global quarter_plane
    if x > 0 and y > 0:
        quarter_plane = 1
    elif x < 0 and y > 0:
        quarter_plane = 2
    elif x < 0 and y < 0:
        quarter_plane = 3
    else:
        quarter_plane = 4
    return quarter_plane


def print_result(quarter_plane):
    # Выводит результат
    print("Точка принадлежит четверти: " + str(quarter_plane))


print_result(find_coordinate_point(taking_coordinates()))
