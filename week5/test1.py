import pandas as pd
import matplotlib.pyplot as plt
import math
# df = pd.read_csv("/Users/bohengwang/Desktop/VSCODEPROJECT/day5/weight-height-data.csv")

# total = 0
# rows = 0
# for index, row in df.iterrows():
#     total += row['Height']
#     rows += 1
# print(total / rows )

x = range(1,10)

y = []

for n in x:
    y.append(math.log(n))

plt.bar(x,y)
plt.show()