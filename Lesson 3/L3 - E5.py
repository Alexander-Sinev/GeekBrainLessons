"""

Эту и шестую задачу не успел доделать, в течение дня постараюсь доделать.

"""


x = 0
a = input("Enter numbers separated by spaces to sum it: ")
b = a.split(' ')

for i in range(len(b)):
    x = x + int(b[i])

print(x)

while(a != 'esc'):
    a = input("Enter numbers separated by spaces to sum it: ")
    b = a.split(' ')
    for i in range(len(b)):
        x = x + int(b[i])

def my_func():
    for i in range(len(b)):
        x = x + int(b[i])


"""    while(a != 'esc'):
        print(my_func)


"""
