from functools import reduce
# using a global value in a functon
x = 0


def A():
    x = 10
    print("x in A:", x)


A()
print("x in global:", x)  # as we saw x has not changed


def B():  # for fixing this problem we use global
    global x
    x = 5


B()
print("x in global:", x)  # now x has changed


# *********************************************************
def c():
    x = 7

    def d():
        nonlocal x  # it's referring to the x in the c() function
        x += 1
        print(x)

    d()


c()


# *********************************************************
# a simple function like len()
def len2(e):
    counter = 0
    for _ in e:
        counter += 1
    return counter


print(len2("tina Hafezi"))
print(len2("1234"))
print(len2([1, 2, 3, 4]))

# *********************************************************
# lambda function
# def func(x):
#    return x**2
f = lambda g: g ** 2
print(f(5))
h = [1, 2, 3, 4]
i = list(map(f, h))  # map sends each item of the list to the function, the return value is map object, so we use list
j = list(map(lambda k: k+2, h))
print(i)
print(j)
l = list(filter(lambda k: k>2,h))  # filter only return values that based on them the return value is true
print(l)
m = reduce(lambda x, y: x*y, h)   # reduce apply a particular function passed in its argument to all the list
print(m)
