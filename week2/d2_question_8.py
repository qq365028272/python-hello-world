numbs = [14,5,19,20,21,66,89]
current = 0
new_sum = 0

print("There are have some numbers below:\n")
for numb in numbs:
    print(numb)

while current < len(numbs):
    new_sum += numbs[current]
    current += 2
print("the Sum of Numbers at Even Indices is: ",new_sum)