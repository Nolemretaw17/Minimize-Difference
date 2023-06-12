import math

text = open("list.txt", "r").readlines()

text.pop(0)
values = text[0].split(" ")

values = sorted([int(element) for element in values])

if len(values) % 2 == 0:
    print(values[int(len(values)/2)])
else:
    print(values[int(math.floor(len(values)/2))])
