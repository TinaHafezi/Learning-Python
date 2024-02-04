a = int(input("a:"))
b = int(input("b:"))
c = []
for i in range(1, min(a, b)+1):
    if ((a % i) == 0) and ((b % i) == 0):
        c.append(i)
print(c)