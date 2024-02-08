a = [1, 2, 3, 4, 5]
b = list(filter(lambda x: x % 2 == 0, a))
print("even numbers:", len(b), "\nodd numbers:", len(a)-len(b))
# *********************************************************
c = [("tina",20), ("paria", 24), ("sarah", 20)]
c.sort(key=lambda x: x[1])
print(c)
# *********************************************************
d = "tina"
e = lambda x: True if x.startswith("t") else False
print(e(d))
