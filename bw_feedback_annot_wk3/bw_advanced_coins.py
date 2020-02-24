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

from functools import reduce
from random import randint

# SJ: This function tosses a single coin, see how we're breaking
# things down into their simplest components?
def toss_coin ():
    flip = randint(0, 2)
    return flip == 0

def toss_n_coins (n):
    # SJ: The _ here is conventionally used when variable name
    # doesn't matter.
    # We're tossing n coins by using a range.
    return [toss_coin() for _ in range(0, n)]

# SJ: This function will group an array `a` in sets of `n`.
def group_up (a, n):
    i = 0
    output = []
    while i <= len(a) - n:
        j = 0
        group = []
        while j < n:
            group += [a[i + j]]
            j += 1
        output += [group]
        i += 1 # SJ: What if we changed this to i += n?
    return output

# SJ: Returns true if all elements in `a` are true.
def all_true (a):
    return reduce(lambda x, y: x and y, a) # SJ: Reduce on Boolean AND to get if all true.

# SJ: Here's a general function that counts all occurrences of m heads in n tosses.
def count_runs_of_m_heads (n, m):
    tosses = toss_n_coins(n) # SJ: Toss n coins.
    groups = group_up(tosses, m) # SJ: Group tosses in groups of m.
    runs_of_true = list(filter(all_true, groups))
    return len(runs_of_true)

# SJ: Now, this function further specialises to triple heads.
def count_triple_heads (n):
    result = count_runs_of_m_heads(n, 3)
    print("Tossed", n, "coins and got", result, "runs of 3 heads.")
