my_f = open('Text.txt', 'w')
line = input('Enter the text: ')

while line != '':
    my_f.writelines(line)
    line = input('Enter the text: ')

my_f.close()
my_f = open('Text.txt', 'r')
content = my_f.readlines()
print(content)
my_f.close()
