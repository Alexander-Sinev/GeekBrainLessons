sentence = input('Enter the sentence: ')
sent_list = sentence.split(' ')

for i in range(len(sent_list)):
    b = i + 1
    
    print(str(b) + '. ' + sent_list[i][0:10])
