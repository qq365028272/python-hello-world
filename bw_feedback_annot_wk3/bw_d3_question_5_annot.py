# Feedback by Saul Johnson <saul.johnson@tees.ac.uk>
# Feedback for: Boheng Wang
#
# **DO NOT REMOVE THIS HEADER**
#
# Notes:
#   + All feedback is marked with "SJ".
#   + This file is for feedback purposes only.
#   + You must use this feedback to guide your own solution.
#     **DO NOT SUBMIT THIS FILE FOR ASSESSMENT**

from random import *

# SJ: I see, so a random sample from a list containing 1-6. Good!
def roll_dice ():
    # SJ: You could also do:
    # dice = range(1, 7)
    dice = [1,2,3,4,5,6]
    dice = sample(dice,1)
    return dice[0]
    # SJ: You could fit this function in one line like this:
    # return randint(1, 6)

# SJ: Again, very good! I will offer some suggestions for efficiency.
def rolls():
    dice_1 = roll_dice()
    dice_2 = roll_dice()
    score = dice_1 + dice_2
    return score
    # SJ: You could fit this function in one line like this:
    # return roll_dice() + roll_dice()

# SJ: Again, excellent. Again, I will offer an efficienty suggestion.
def print_star(time):
    a = 0
    while a < time:
        print('*',end ="")
        a += 1
    # SJ: You could fit this function in one line. Remember, Python
    # strings support multiplication:
    # return '*' * time

this_time = int(input("Plese input the time of roll: "))

# SJ: This is a perfectly acceptable way to do it, nice!
list_score = [0,0,0,0,0,0,0,0,0,0,0]
n = 0
while n < this_time:
    this_score = rolls()
    # SJ: Because the array index is always 2 less than the score,
    # consider this one-liner instead:
    # list_score[this_score - 2] = this_score
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
