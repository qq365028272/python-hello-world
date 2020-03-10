from functools import reduce


def cars_exercise():
    with open("cars_exercise_3.txt", mode="r") as Car_flie:
        the_lst = []
        for line in Car_flie:
            line = line.rstrip("\n")
            the_lst.append(line)
        i = 0
        new_dict = []
        while i < len(the_lst):
            new_dict.append(
                {"Make": the_lst[i], "Model": the_lst[i+1], "Year": the_lst[i+2]})
            i += 3
        return new_dict


def compare_max(p1, p2):
    if p1['Year'] >= p2['Year']:
        return p1
    else:
        return p2


def compare_min(p1, p2):
    if p1['Year'] >= p2['Year']:
        return p2
    else:
        return p1


y = cars_exercise()

max_mp = reduce(compare_max, y)
min_mp = reduce(compare_min, y)

print("The newest year is :", max_mp)
print("The oldest year is :", min_mp)