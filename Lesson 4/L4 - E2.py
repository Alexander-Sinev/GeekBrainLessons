my_list = [6, 3, 7, 10, 2, 63, 17, 20]
new = [el for el in my_list if el > my_list[my_list.index(el)-1]]
print(new)
