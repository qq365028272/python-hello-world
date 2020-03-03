import matplotlib.pyplot as plt
import math
import random   

random_lst1 = []
random_lst2 = []
n = 0
while n < 10:
    random_lst1.append(random.randint(1,10))
    random_lst2.append(random.randint(1,10))
    n += 1

plt.scatter(random_lst1, random_lst2)
plt.show()