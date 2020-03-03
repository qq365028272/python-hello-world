import pandas as pd
import matplotlib.pyplot as plt
import random
import csv

f = open('/Users/bohengwang/Desktop/VSCODEPROJECT/week5/aa.csv','w',encoding='utf-8')
csv_writer = csv.writer(f)
csv_writer.writerow(["Times","Result"])

coin_range = range (1,50001)
coin_tosses = []

for roll in coin_range:
    roll_numb = random.choice(['True','False'])
    coin_tosses.append(roll_numb)
    csv_writer.writerow([roll,roll_numb])

f.close()

