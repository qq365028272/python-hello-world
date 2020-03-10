import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("weight-height-data.csv")
whrs = []
for i, row in df.iterrows():
    whr = row["Weight"] / row["Height"]
    whrs.append(whr)
df["WHR"] = whrs
df.to_csv("whr-data.csv")

whr_df = pd.read_csv("whr-data.csv")

plt.xlabel("Height")
plt.ylabel("WHR")
plt.title("WHR analyze")
plt.scatter(whr_df['Height'],whr_df['WHR'])
plt.show()