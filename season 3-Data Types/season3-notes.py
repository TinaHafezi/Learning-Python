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
j.append(['t', 'g'])
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
r = {
    "1": {"name": 'fd', "age": 23},
    "2": {"name": 'df', "age": 23}
}
print(r)
s = ["a", "b"]
t = [20, 12]
w = dict(zip(s, t))  # zip two list together
print(w)

# set
x = {1, 2, 3, 2, 3, 4, 2}  # set do
print(len(x))
x.add(6)
print(x)
x.remove(6)  # we can remove values that already exit
x.discard(12)
x.discard(2)  # but with discard we can remove anything
print(x)
y = {1, 2, 5, 67, 34}
print(x-y)
print(x.difference(y))
print(x | y)  # x+y
print(x.union(y))
print(x & y)
print(x.intersection(y))
print(x ^ y)  # (x|y)-(x&y)
print(x.symmetric_difference(y))  # (x-y) | (y-x)
print(x < y)  # is x sub set of y?
print(x.issubset(y))
# false: [],(),{},"",set(),none,0 ==> all of these when are empty are considered as false
print(bool({}))
print(bool(str("0")))
# using "and" "or" with just values and not using any compare
# if(x and y)
# if x is true==>y
# if x is false==>x
print(5 and [])
# if(x or y)
# if x is true==>x
# if x is false==>y
print(5 or [])
print(5 or 0 == 6)  # even when we are using a single value and a compression the form is the same
