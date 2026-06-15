def is_year_leap(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0:
        return True
    else:
        return False


year = int(input("Введите год: "))
print(is_year_leap(year))
