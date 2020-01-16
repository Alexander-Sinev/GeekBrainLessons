x = int(input("Enter the REAL number: "))
y = int(input("Enter the NEGATIVE number: "))

def my_func(x, y):
    return x**y

print(my_func(x, y))


###------------------------------------------------------------

x = int(input("Enter the REAL number: "))
y = int(input("Enter the NEGATIVE number: "))

def my_func(x, y):
    a = x
    if y < 0:
        for i in range(y * (-1) - 1):
            a = a * x
        return 1 / a
    elif(y == 0):
        return 1
    else:
        for i in range(y - 1):
            a = a * x
        return a

print(my_func(x, y))
