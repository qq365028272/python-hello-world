from random import *

rucksack = ['Water flask',  #0 水瓶\ 
            'Cheese',   #1 起司\
            'Gold coins',   #2 金币\
            'Handkerchief', #3 手帕\
            'Tinderbox',    #4 火种箱\
            'Scrolls',  #5 卷轴\
            'Dagger',   #6 匕首\
            'Rope', #7 绳\
            'Nuts', #8 坚果\
            'Pipe', #9 管道\
            'Tobacco',  #10 烟草\
            'Wine skin',    #11 酒皮\
            'Herbs',    #12 草药\
            'Axe',] #13 斧头

def how_many ():
    j = 0
    for i in rucksack:
        j +=1
    return j

def add_ (goods):
    return rucksack.append(goods)

rucksack.sort()
print(rucksack)

print("numbs: ",how_many())

add_('Gems')
add_('Necklace')
rucksack.sort()
print(rucksack)

def random_del():
    y = sample(rucksack,5)
    list3 = [i for i in rucksack if i not in y]
    return list3

print(random_del())