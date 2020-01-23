num = input('Enter numbers: ')
summ = open('Text5.txt', 'w')
summ.writelines(num)

try:
    with open('Text5.txt', 'r') as file_obj:
        line = num.split()
        print(sum(map(int, line)))

except IOError:
        print('File Error!')
except ValueError:
        print('Wrong number! Enter Error!')

summ.close()
