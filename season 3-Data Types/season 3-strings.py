i = 'c\Dawnload\gew'  # whenever we want to cancel the effect of something(any character that effects string)
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

# string format
p = 2
print("p is%i and %s" % (p, "salam"))  # a way for adding values in the string i=>int s=>string
print("sajfak: {} ajaslkj:{} akjfaj:{}".format(4, 5, 6))  # another format, in {} we set the index of arg
print("sajfak: {2} ajaslkj:{1} akjfaj:{1}".format(4, 5, 6))
print("sajfak: {2} ajaslkj:{2} akjfaj:{2}".format(4, 5, 6))
q = {'a': 2, 'b': 3, 'c': 34}
print("sajfak: {a} ajaslkj:{b} akjfaj:{c}".format(**q))
print("sajfak: {x} ajaslkj:{y} akjfaj:{z}".format(x=q['a'], y=q['b'], z=q['c']))
print("sajfak: {0} ajaslkj:{2} akjfaj:{1}".format(*'tina'))
print("sajfak: {0} ajaslkj:{2} akjfaj:{1}".format(*[4, 5, 6]))
# for more options in this type of format watch sabzlearns03-e10
print(f'q is {q}')  # we put f before "" then add {} wherever we want and then put the value in it
