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

def toss_coin():
    coin_face = randint(1,2) # SJ: Perfect, this is exactly the right approach.
    return coin_face
    # SJ: The sides of a coin are ideally suited to Boolean values. True for heads
    # and false for tails.
    # return coin_face == 1 # SJ: 1 means heads, 2 means tails!

# SJ: I can see what you're trying to do here, but let's try something else...
def long_head(_face,n):
    if _face == 1:
        n += 1

# SJ: Here's a function I've written to toss 1 coin.
def toss_coin_sj():
    return randint(0,1) == 0

# SJ: Here's a function I've written to toss n coins.
def toss_coins_sj(n):
    # Let's use a list comprehension to make this simple:
    return [toss_coin_sj() for _ in range(0, n)]
    # Try running this function by itself in the REPL to see how it works!

# SJ: And finally, here's an example
def count_longest_heads_run_sj(n):
    # First, toss n coins:
    coins = toss_coins_sj(n)
    # Now, we need to get the longest run of True in this array.
    run = 0
    longest = 0
    for coin in coins:
        if coin == False: # When we meet _na tails...
            longest = max(longest, run) # Remember longest run.
            run = 0 # Reset the run, it's been broken.
        else:
            run += 1 # It's a heads! Extend run by 1.
    # We need to do this one more time because we may have ended on a heads.
    return max(longest, run)

# SJ: What's below here seems to be debugging code that you will be able
# to improve by taking the above into account!

# def toss_coin():
#     coin_face = randint(1,2)
#     return coin_face
#
# def long_head(_face,n):
#     if _face == 1:
#         n += 1
#     else:
#         return n
#
# def long_tail(_face2,m):
#     if _face2 == 2:
#         m +=1
#     else:
#         return m
#
# for i in range(1,6):
#     for j in range(1,21):
#         this_face = int(toss_coin())
#         if this_face == 1:
#             print('H',end = "")
#         else:
#             print('T', end = "")
#     print('\n')
#
#
#
#     else:
#         return n
#
# def long_tail(_face2,m):
#     if _face2 == 2:
#         m +=1
#     else:
#         return m
#
# for i in range(1,6):
#     for j in range(1,21):
#         this_face = int(toss_coin())
#         if this_face == 1:
#             print('H',end = "")
#         else:
#             print('T', end = "")
#     print('\n')
