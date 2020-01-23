firm = {'Black': 25000, 'White': 18500, 'Blue': 12000, 'Green': 20000}
try:
    file_obj = open("Text3.txt", 'w')
    for last_name, salary in firm.items():
        file_obj.write(last_name + ':' + str(salary) + "\n")
except IOError:
    print("Enter Error!")
finally:
    file_obj.close()
summ = 0
count = 0
lowpay = []
with open("Text3.txt", "r") as file_obj:
    for line in file_obj:
        print(line, end="")
        tokens = line.split(':')
        if int(tokens[1]) < 20000:
            lowpay.append(tokens[0])
        summ += int(tokens[1])
        count += 1
result = summ / count
print(f"persons: {lowpay}")
print(f"averate: {result}")
