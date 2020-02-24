from datafile import data
from functools import reduce

def pair_up (lst):
    i = []
    n = 0
    while n < len(lst):
        i.append({"name": lst[n],"score": lst[n+1]})
        n += 2
    return i

new_data = pair_up(data)

max_score = reduce(lambda x,y : x if x["score"] > y["score"] else y , new_data)

print(max_score)