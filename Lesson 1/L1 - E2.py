t = int(input("Enter time in seconds: "))

s = t % 60
t = t // 60
m = t % 60
h = t // 60

if (s < 10):
    s = "0" + str(s)
if (m < 10):
    m = "0" + str(m)
if (h < 10):
    h = "0" + str(h)

print(f"Time is: {h}:{m}:{s}")
