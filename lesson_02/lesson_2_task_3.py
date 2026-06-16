import math


def square(a):
    a2 = a * a
    return math.ceil(a2)


a = float(input("Введите сторону квадрата: "))
print(f"Площадь квадрата равна: {square(a)}")
