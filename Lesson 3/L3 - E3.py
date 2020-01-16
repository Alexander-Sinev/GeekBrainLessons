def my_func(arg_1, arg_2, arg_3):
    lis = [arg_1, arg_2, arg_3]
    lis.remove(min(lis))
    summ = lis[0] + lis[1]
    return summ

print(my_func(int(input("Enter the first number: ")),
              int(input("Enter the second number: ")),
              int(input("Enter the third number: "))))
