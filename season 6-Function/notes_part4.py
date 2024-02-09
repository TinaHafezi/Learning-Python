def gen_range(start, end, step=1):
    while start < end:
        yield start
        start += step


a = gen_range(10, 20, 2)
print(list(a))


# *********************************************************
def gen(r):
    for i in range(r):
        yield i ** 2


b = list(gen(10))
print(list(b))
print(sum(b))
print(max(b))
c = gen(10)


# c.send()
# c.close()
# c.throw()


# *********************************************************
# coroutine
def my_gen():
    while True:
        x = yield
        print("my name is ", x)


d = my_gen()
next(d)
d.send("tina")


# *********************************************************
# generator without next using decorator
def gen_decorator(gen1):
    def inner():
        ge = gen1()
        next(ge)
        return ge

    return inner


@gen_decorator
def gen_dec():
    while True:
        x = yield 1
        print("my name is", x)


e = gen_dec()
e.send("tina")


# *********************************************************
# adding attribute
def func(x):
    return sum(x) / len(x)


func.new_attribute = "something"
setattr(func, "something", "somthing")
print(dir(func([1, 2, 3])))
print(func.new_attribute)
print(func.__dict__)
delattr(func, "something")
print(func.__dict__)


# *********************************************************
# fib with memory
def gen_memory(fib):
    memory = {}

    def inner(n):
        if n not in memory:
            memory[n] = fib(n)
        return memory[n]
    return inner


@gen_memory
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(100))  # a faster way than using recursive fib without decorator
