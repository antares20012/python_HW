lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]


def funk():
    for num in sorted(lst):
        if num < 30 and num % 3 == 0:
            print(num)


funk()
