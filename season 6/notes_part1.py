def f(a, b, c):
    print("a:", a, end=" ")
    print("b:", b, end=" ")
    print("c:", c)


# usual way
f(1, 2, 3)
d = [1, 2, 3, 4]
f(1, 2, d)
# name = value
f(b=3, a=1, c=2)
# *iterable  (str, tuple, list, set...)
x = [1, 2, 3]
f(*[1, 2, 3])
f(*x)


# *********************************************************
def f2(a=1, b=2, c=3):
    print("a:", a, end=" ")
    print("b:", b, end=" ")
    print("c:", c)


# having default value
f2()
f2(b=5, c=1)


# *********************************************************
def f3(a, b, *c):
    print("a:", a, end=" ")
    print("b:", b, end=" ")
    print("c:", c)


f3(1, 2, 3, 4, 5, 6, 7, 8)


# *********************************************************
# dictionary as parameter
def f4(**a):
    print("a:", a)


f4(a=1, b=2, c=3)


# *********************************************************
def f5():
    """here in the first line of the function, we wrote docstring"""
    return 1


print(f5.__doc__)


# *********************************************************
# using annotation for parameter and return value
def f6(a: int, b=3) -> tuple:
    return a + b, a, b


print(f6(1))  # f6("1") is wrong because the argument should be int
print(f6.__annotations__)
