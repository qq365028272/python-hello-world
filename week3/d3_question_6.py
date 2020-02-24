from random import *

def toss_coin():
    coin_face = randint(1,2)
    return coin_face

def long_head(_face,n):
    if _face == 1:
        n += 1
    else:
        return n

def long_tail(_face2,m):
    if _face2 == 2:
        m +=1
    else:
        return m

for i in range(1,6):
    for j in range(1,21):
        this_face = int(toss_coin())
        if this_face == 1:
            print('H',end = "")
        else:
            print('T', end = "")
    print('\n')


