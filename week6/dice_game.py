# Code by Saul Johnson <saul.johnson@tees.ac.uk>
# This code example is for an excercise.
#
# **DO NOT REMOVE THIS HEADER**
#
# Notes:
#   + This file is for demonstration purposes only.
#   + You must use this file to **GUIDE** your own solution.
#     **DO NOT SUBMIT THIS FILE FOR ASSESSMENT**

from random import randint


# Rolls a 6-sided die.
def roll_dice():
    return randint(1, 6)


# Returns the values yielded by rolling n 6-sided dice.
def roll_n_dice(n):
    return [roll_dice() for _ in range(0, n)]


# Counts the frequency of each score from rolling n 6-sided dice.
def count_roll_freqs(n):
    out = [0 for _ in range(0, 6)]
    for roll in roll_n_dice(n):
        out[roll - 1] += 1
    return out


# A function that prints out the score card and returns points.
# Points are the maximum number of times the same number was rolled.
def total_score(scores):
    i = 0
    while i < len(scores): # Loop, printing score card.
        print("\tThe number", i + 1, "a total of", scores[i], "times!")
        i += 1
    points = max(scores) # Get maximum number of times same number rolled.
    print("You rolled the same number a maximum of ", points, "times!")
    return points    


# Loop until players quit.
play_again = True
while play_again:
    
    # Get name of player 1, greet them and roll their dice.
    player_1_name = input("Player 1, enter your name and press enter to roll: ")
    print("Great to see you,", player_1_name)
    player_1_rolls = count_roll_freqs(12) # Roll 12 dice.

    # Show player 1 scores.
    print("Player 1, you rolled:")
    player_1_points = total_score(player_1_rolls)

    # Get name of player 2, greet them and roll their dice.
    player_2_name = input("Player 2, enter your name and press enter to roll: ")
    print("Great to see you,", player_2_name)
    player_2_rolls = count_roll_freqs(12) # Roll 12 dice.

    # Show player 2 scores.
    print("Player 2, you rolled:")
    player_2_points = total_score(player_2_rolls)

    # Show winner.
    if player_1_points > player_2_points:
        print("Player 1 wins!")
    elif player_2_points > player_1_points:
        print("Player 2 wins!")
    else:
        print("It's a draw!")

    # Ask to play again.
    play_again = input("Another round? [yes/no] ").lower().startswith("y")

