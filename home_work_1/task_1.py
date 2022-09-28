"""
Задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
является ли этот день выходным.
"""


def check_day_weekend(number_day):
    # определяем является ли день выходным
    if(number_day == 6 or number_day == 7):
        return True
    else:
        return False


def check_day_of_week(number_day):
    # проверяет корректность введенного дня недели
    if(number_day <= 0 or number_day > 7):
        print("Такого дня недели не существует")
        check_day()
    else:
        return number_day


def print_result(result):
    # печатает результат в консоль
    if(result):
        print('Выходной день')
    else:
        print('Будний день')


def check_day():
    try:
        number_day = int(input('Введите номер дня недели: '))
        print_result(check_day_weekend(check_day_of_week(number_day)))
    except:
        print('Необходимо вводить цифры')
        check_day()


check_day()




