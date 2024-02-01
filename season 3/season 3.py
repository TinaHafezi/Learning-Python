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

i = "c:\Dawnload\gew"  # whenever we want to cancel the effect of something(any character that effects string)
# we use extra backslash
j = r"c:\Dawnload\new\telegram"  # "r" cancels all the special codes in the string such as \n and \t
k = """\
ti
sa
ma\
"""  # it's helpful for printing lists
print(i)
print(j)
print(k)

# a simple way for back setting a number
l = "123456789"
print(l[::-1])

# string methods
m = "tina"
print(len(m))
print(m.upper())
print(m.lower())
print(m.count('n'))
print(m.endswith('n'))
print(m.startswith('n'))
print(m.find('n'))  # return the index of the first character that it found
print(m.rfind('n'))  # return the index of the last character that it found
print(m.isalnum())  # are all the characters number and character
print(m.isnumeric())  # are all the characters number
n = "tina,sara,paria"
print(n.split(','))
print(n.replace(",","+"))
print(ord("a"))  # the unicode of the character
print(chr(97))  # the character of the unicode
print("s: \u0489")  # \u for adding special characters that are not in the keyboard
