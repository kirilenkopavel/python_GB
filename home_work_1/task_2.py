"""
Задача 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
"""


def input_numbers(x):
    # принимает значения предикант
    xyz = ["X", "Y", "Z"]
    a = []
    for i in range(x):
        a.append(input(f"Введите значение {xyz[i]}: "))
    return a


def check_predicate(x):
    # проверяет условия предикант
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result


def print_result():
    if (check_predicate(input_numbers(3))):
        print(f"Утверждение истинно")
    else:
        print(f"Утверждение ложно")


print_result()

