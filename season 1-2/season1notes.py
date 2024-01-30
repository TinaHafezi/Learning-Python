# season one notes

# changing variables in python
a = 4
b = 5
a, b = b, a
print("a:", a, "b:", b)

# "is" and "=="
c = 5
d = 5
print(c == d)
print(c is d)
e = [1, 2, 3]
f = [1, 2, 3]
print(e == f)
print(e is f)  # it's because they are not stored in the same place
print(id(e))
print(id(f))

# binary numbers/ for more examples of binary operators check the Sabzlearn-S02E14
g = 0b0101
print(bin(a))
print(g)

# walrus
print(h := 2)  # print(h = 2) is not correct
