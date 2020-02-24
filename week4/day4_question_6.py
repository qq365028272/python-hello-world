def change_form():
    the_lst = []
    with open("/Users/bohengwang/Desktop/VSCODEPROJECT/day4/cars_exercise_6.txt", mode="r") as Car_flie:
        for line in Car_flie:
            line = line.rstrip("\n")
            the_lst.append(line)
    i = 1
    while i < len(the_lst):
        the_lst[i] = the_lst[i+1]+the_lst[i]
        i += 3
    j = 2
    while j <= len(the_lst):
        del the_lst[j]
        j += 2

    with open("Change_form.txt", mode="w") as my_form:
        for line in the_lst:
            my_form.write(line+"\n")


change_form()
