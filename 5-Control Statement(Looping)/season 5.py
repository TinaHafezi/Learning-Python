from random import random, uniform
from random import randint
from random import choice
from random import sample

for i in range(2, 10):  # range(start, end, indexer)
    print(i, end=" ")
print()

# reversing a number
a = input("n:")
for i in range(len(a)-1,-1,-1):
    print(a[i],end="")
print()

b = ["a", "b", "c", "d"]
for i, j in enumerate(b):
    print(i, ":", j)

c = ["tina", "sara", "paria"]
d = [20, 20, 24]
for i, j in zip(c,d):
    print("namr:", i, "age:", j)

print(5 + random()*(15-5))
print(uniform(5, 15))
print(randint(5, 16))
print(choice(c))  # choose a random item from the list
print(sample(c, 2))  # make a sample

# random dice
dice = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
for _ in range(1000):
    dice[randint(1, 6)] += 1
print(dice)