def cars_exercise ():
    with open("/Users/bohengwang/Desktop/VSCODEPROJECT/day4/cars_exercise_3.txt", mode = "r") as Car_flie:
        the_lst = []
        for line in Car_flie:
            line = line.rstrip("\n")
            the_lst.append(line)
        return the_lst

def write_file ():
            i = 0
            n = 2
            a = 0
            cars = cars_exercise()
            while n <= len(cars):
                fname = cars[a]+'_'+cars[a+1]+'_'+cars[a+2]+'.txt'
                with open(fname, mode = "w") as my_flie:
                    while i <= n:
                        my_flie.write(cars[i] + "\n")
                        i += 1
                n += 3
                a += 3

write_file()

                

