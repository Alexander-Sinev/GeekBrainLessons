n = int(input("Enter the number: "))

m = n % 10
n = (n // 10)
while(n > 0):
    if (m < n % 10):
        m = n % 10
        n = (n // 10)
    else:
        n = (n // 10)

print(m)
