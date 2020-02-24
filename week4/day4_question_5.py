def years_lst ():
    the_lst = []
    with open("/Users/bohengwang/Desktop/VSCODEPROJECT/day4/cars_exercise_del.txt", mode = "r") as Car_flie:
        for line in Car_flie:
            line = line.rstrip("\n")
            the_lst.append(line)
    i = 2
    year_lst = []
    while i <= len(the_lst):            
        year_lst.append(the_lst[i])
        i += 3
    return year_lst

def years_del (term):
    the_lst = []
    with open("/Users/bohengwang/Desktop/VSCODEPROJECT/day4/cars_exercise_del.txt", mode = "r") as Car_flie:
        for line in Car_flie:
            if not term in line:
                the_lst.append(line)
    with open("/Users/bohengwang/Desktop/VSCODEPROJECT/day4/cars_exercise_del.txt", mode = "w" ) as no_year_lst :
        for line in the_lst:
                no_year_lst.write(line)

for n in years_lst():
    years_del(n)

