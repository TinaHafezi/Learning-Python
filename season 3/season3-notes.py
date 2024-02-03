import fractions

# Data types
a = {1, 2, 3, 4}  # set
b = (1, 2, 3, 4)  # tuple
c = [1, 2, 3, 4]  # list

print(fractions.Fraction(.75))

d = 1_000_000_000_000_000  # a simple way for typing big numbers
e = 1e15  # 1 * 10**15
f = 1e+15  # same as the line above
print(d == e == f)
g = 2e-15
print(g)  # there is a limit for mantissa in float numbers using scientific notation
h = 1e-3
print(h)

# a simple way for back setting a number
i = "123456789"
print(i[::-1])

# list
j = [1, 2, ['a', 3], 4]
print(j[2][1])
j.append(['t','g'])
print(j)
k, l, *m = [1, 2, 3, 4, 5, 5]
print(k, ' ', l, ' ', m)

# tuple
n = (1, 2, 3, 4)  # tuple values cant change but if thr value type is list, we can change the value in the list
o = 1, 2, 3, 4
print(type(o))

# dictionary
p = {"a": 12, "b": [1, 2, 3]}
print(p["b"])
p["c"] = 5  # adding new keys and values
print(p)
print(p.values())  # return a list of values
print(p.keys())
print(p.items())
del p['b']
print(p)
print(sorted(p.values()))
q = dict([('a', 12), ('b', 23), ('c', 1)])  # dictionary items are tuple so for making a dict we can add tuples
print(q)
r ={
    "1": {"name": 'fd', "age": 23},
    "2": {"name": 'df', "age": 23}
}
print(r)
