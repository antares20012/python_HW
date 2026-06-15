def month_to_season(month):
    if month >= 1 and month <= 2 or month == 12:
        print("Зима")
    elif month >= 3 and month <= 5:
        print("Весна")
    elif month >= 6 and month <= 8:
        print("Лето")
    elif month >= 9 and month <= 11:
        print("Осень")
    else:
        print("Введите номер месяца от 1 до 12")


month = int(input("Введите номер месяца: "))
month_to_season(month)
