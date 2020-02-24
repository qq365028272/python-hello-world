def chose_recursion ():
    type_form = int(input("Please type 1 for sphere, 2 for cylinder and 3 for cone:  "))
    if type_form == 1:
        print("sphere")
    elif type_form == 2:
        print("cylinder")
    elif type_form == 3:
        print("cone")
    else:
        print("this number is invaild, plese try again: ")
        choose_recursion()


choose_recursion() 