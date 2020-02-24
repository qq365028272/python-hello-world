from random import*

n = 0
list_random = []
while n < 20:
    random_numb = randint(0,99)
    list_random.append(random_numb)
    n += 1
print(list_random)

max_value = max(list_random)
min_value = min(list_random)
list_random.remove(max_value)
list_random.remove(min_value)

second_max = max(list_random)
second_min = min(list_random)

list_random.append(max_value)
list_random.append(min_value)

print(second_max,"  ",second_min)  