l = []
el = 0

q = input("Enter list element or 'end': ")

while (q != 'end'):
    l.append(q)
    q = input("Enter list element or 'end': ")


for i in range(int(len(l) / 2)):
    l[el], l[el + 1] = l[el + 1], l[el]
    el += 2
