my_list = [7, 5, 3, 3, 2]
inp = ()
i = 0

print(my_list)

while (inp != 'end'):
    inp = input('Enter the rating number (end - exit): ')
    if (inp == 'end'):
        break
    inp = int(inp)
    for n in range(len(my_list)):
        if (inp < my_list[-1]):
            my_list.append(inp)
            break
        elif (inp == my_list[n]):
            while (inp == my_list[n]):
                n = n + 1
            my_list.insert(n, inp)
            break
        elif (inp > my_list[0]):
            my_list.insert(0, inp)
            break
        elif (my_list[n] > inp and inp > my_list[n+1]):
            my_list.insert(n + 1, inp)
            break

print(my_list)
