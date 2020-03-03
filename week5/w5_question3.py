import matplotlib.pyplot as plt

def squared(x):
    return x**2

range_lst = range(-500,501)

sq_lst = []
for n in range_lst:
    sq_lst.append(squared(n))

plt.plot(range_lst, sq_lst, ls = "-", lw = 2, label = "plot figure")
plt.show()
