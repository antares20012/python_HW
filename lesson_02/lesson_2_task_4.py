def fizzbuzz(n):

    for n in range(1, n + 1):
        if n % 3 == 0 and n % 5 == 0:
            print("fizzbuzz")
        elif n % 5 == 0:
            print("buzz")
        elif n % 3 == 0:
            print("fizz")
        else:
            print(n)


n = int(input("Введите число: "))
fizzbuzz(n)
