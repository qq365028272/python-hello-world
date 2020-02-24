def inc_list(lst):
    i = 0
    while i < len(lst):
        lst[i] = lst[i] + 1
        i += 1
    return lst

def inc_listp(lst):
    i = 0
    n = []
    while i < len(lst):
        n += [lst[i] + 1]
        i += 1
    return n

# y = [1,2,3,4,5,6,7,8]

# # print(inc_list(y))
# # print(inc_listp(y))

# new_y = y[1:len(y):2]

# print(new_y)