my_list = ['Hello\n', 'World\n', 'Programming\n']

with open("Text2.txt", 'w+') as file_obj:
    file_obj.writelines(my_list)
with open("Text2.txt") as file_obj:
    lines = 0
    letters = 0
    for line in file_obj:
        lines += line.count("\n")
        letters = len(line)-1
        print(f"{letters} letters in line")
    print(f"String count is {lines}")
