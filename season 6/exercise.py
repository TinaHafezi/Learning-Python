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
# *********************************************************
# generator
f = ["a", "b", "c"]
for i, j in enumerate(f):   # how enumerate works
    print(i, j)


def gen_enumerate(lst, start=0):
    for x in lst:
        yield start, x
        start += 1


for i, j in gen_enumerate(f):
    print(i, j)


# *********************************************************
def gen_fibonacci(n):
    f1 = 0
    yield f1
    f2 = 1
    yield f2
    for _ in range(n-2):
        f3 = f1 + f2
        yield f3
        f1 = f2
        f2 = f3


for i in gen_fibonacci(10):
    print(i)


# *********************************************************
def gen_rev(str):
    l = len(str)
    for i in range(l-1, -1, -1):
        yield str[i]


for i in gen_rev("tina"):
    print(i)


# *********************************************************
def gen_cen(words):
    answer = None
    while True:
        word = yield answer
        if word not in words:
            answer = word
        else:
            answer = "*"*len(word)


j = gen_cen(["khar", "gav", "moosh"])
next(j)
print(j.send("tina"))
print(j.send("sara"))
print(j.send("khar"))
print(j.send("paria"))
