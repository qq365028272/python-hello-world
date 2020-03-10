from random import*

n = 0
list_random = []
while n < 20:
    random_numb = randint(0,99)
    list_random.append(random_numb)
    n += 1
print(list_random)

list_random.insert(10,50)

print(list_random)

n = 0
index_ = 0
while n < 10:
    if list_random[index_] > 50 :
        y = list_random[index_]
        list_random.pop(index_)
        list_random.append(y)
    else:
        index_ += 1
    n += 1

print(list_random)


m = index_ + 1
new_index = index_ + 1
while m < len(list_random):
    if list_random[new_index] < 50 :
        h = list_random[new_index]
        list_random.pop(new_index)
        list_random.insert(0,h)
    else:
        new_index += 1
    m += 1

print(list_random) 
