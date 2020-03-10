from functools import reduce


def cars_exercise():
    with open("cars_exercise_6.txt", mode="r") as Car_flie:
        the_lst = []
        for line in Car_flie:
            line = line.rstrip("\n")
            the_lst.append(line.lower())
        i = 0
        new_dict = []
        while i < len(the_lst):
            new_dict.append(
                {"Make": the_lst[i], "Model": the_lst[i+1], "Year": the_lst[i+2]})
            i += 3
        return new_dict

def cars_write():
    with open("cars_exercise_6.txt", mode = "w") as Car_write_file:   
        y = cars_exercise()
        for line in y:
            Car_write_file.append(line)

print(cars_write())
print("These are cars' details below:")
ask_add_or_del = input("If you want to add the car ,plese input 'Yes', or delete the car ,input 'No':")
if ask_add_or_del == 'Yes':
    print("Plese input the 'Make', 'Model' and 'Year'. ")
    

elif ask_add_or_del == 'No':
    pass

else:
    print("You input is error.")

print(y)