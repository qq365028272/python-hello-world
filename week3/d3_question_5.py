from random import *

def roll_dice ():
    dice = [1,2,3,4,5,6]
    dice = sample(dice,1)
    return dice[0]

def rolls():
    dice_1 = roll_dice()
    dice_2 = roll_dice()
    score = dice_1 + dice_2
    return score

def print_star(time):
    a = 0
    while a < time:
        print('*',end ="")
        a += 1

this_time = int(input("Plese input the time of roll: "))

list_score = [0,0,0,0,0,0,0,0,0,0,0]
n = 0
while n < this_time:
    this_score = rolls()
    if this_score == 2:
        list_score[0] += 1
    elif this_score == 3:
        list_score[1] += 1
    elif this_score == 4:
        list_score[2] += 1
    elif this_score == 5:
        list_score[3] += 1
    elif this_score == 6:
        list_score[4] += 1
    elif this_score == 7:
        list_score[5] += 1
    elif this_score == 8:
        list_score[6] += 1
    elif this_score == 9:
        list_score[7] += 1
    elif this_score == 10:
        list_score[8] += 1
    elif this_score == 11:
        list_score[9] += 1
    else:
        list_score[10] += 1
    n += 1

j = 1
i = 0
while j <= len(list_score):
    print("Score: ",j+1, "Rolls: ", list_score[i],end = "")
    print_star(list_score[i])
    print('\n')
    j += 1
    i += 1



