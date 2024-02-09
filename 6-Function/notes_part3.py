from itertools import count
from time import perf_counter

# iterator => first we check if the value is iterable
a = [1, 2, 3]
print("__iter__" in dir(a))
print("__next__" in dir(a))  # as we can see it is not iterator yet
# then we use iter method to make it iterator
a = iter(a)
while True:
    try:
        print(next(a))

    except StopIteration:
        break
# *********************************************************
# it's a endless iterator and it is lazy
b = count()


# for i in b:
#    print(i)


# *********************************************************
# decorator
def dec(function1):
    def inner(x, y):
        if y == 0:
            print("warning!!")
        else:
            function1(x, y)

    return inner


@dec
def func(x, y):
    print(x / y)


func(6, 3)
func(6, 0)


# *********************************************************
# using multiple decorators
def star(msg1):
    def inner(*x, **y):
        print("*" * 20)
        msg1(*x, **y)
        print("*" * 20)

    return inner


def dash(msg1):
    def inner(*x, **y):
        print("-" * 20)
        msg1(*x, **y)
        print("-" * 20)

    return inner


@dash
@star
def msg(name):
    print("I am" + name)


msg("Tina")


# *********************************************************
def star2(d):
    def inner(func1):
        def inner2(*x, **y):
            print("*" * d)
            func1(*x, **y)
            print("*" * d)

        return inner2

    return inner


@star2(5)
def msg2(name):
    print("I am", name)


msg2("Tina")
# *********************************************************
passwords = {"tina": "1234", "sara": "1234", "paria": "1234"}
blocked = {"sara"}


def ban(change_pass):
    def inner(*x, **y):
        if x[0] in blocked:
            print("this user can not change password")
        else:
            change_pass(*x, **y)

    return inner


@ban
def changePass(username, userpass):
    passwords[username] = userpass


changePass("sara", "2345")
print(passwords)


# *********************************************************
# function timecalculator
def calculator(func1):
    def inner(*x, **y):
        start_time = perf_counter()
        value = func1(*x, **y)
        end_time = perf_counter()
        run_time = end_time - start_time
        print("run time", func1.__name__, "is:", run_time)
        return value

    return inner


@calculator
def f(x):
    for i in range(x):
        i *= 2


f(20)
