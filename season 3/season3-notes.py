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
l = "123456789"
print(l[::-1])
