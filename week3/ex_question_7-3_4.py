from random import*

n = 0
list_random = []
while n < 20:
    random_numb = randint(0,99)
    list_random.append(random_numb)
    n += 1
print(list_random)

for n in (1,2):
    old_numb = max(list_random)
    print("To be removed before: ",old_numb)
    list_random.remove(old_numb)

print(list_random)

def apply_to_list(old_list):
    new_list = []
    for item in old_list:
        new_list.append(item)
    return new_list

y = apply_to_list(list_random)
for i in (1,2):
    y.append(randint(0,99))

print(y)

