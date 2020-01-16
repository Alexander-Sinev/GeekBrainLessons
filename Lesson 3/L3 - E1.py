def fun(arg_1, arg_2):
    if(arg_2 == 0):
        return "You can't divide by zero!"
    else:
        return arg_1 / arg_2

print(fun(int(input("Enter first number: ")), int(input("Enter second number: "))))
