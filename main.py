try:
    a = int(input("Введіть перше число:"))
    b = int(input("Введіть перше число:"))
    c = a/b
    print(c)
except ZeroDivisionError:
    print('На 0 ділити не можна')
