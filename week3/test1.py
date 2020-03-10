from random import *

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

x = sample(items,  1)   # Pick a random item from the list
print(x[0])

y = sample(items, 4)    # Pick 4 random items from the list
print(y[0])

print(random())