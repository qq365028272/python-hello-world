def ask_question ():
    x = float(input("pls input a number x: "))
    y = float(input("pls input a number y: "))
    enter = int(input("pls input 1(to add), 2(to subtract),3(to multiply) or 4(to divide)"))
    if enter == 1:
        print(x+y)
    elif enter == 2:
        print(x-y)
    elif enter == 3:
        print(x*y)
    elif enter == 4:
        print(x/y)
    else :
        print("your enter is error.")
    con_tinue = input('do you want to continue? if u want ,pls enter "yes", if u don\'t, pls enter "no": ' )
    if con_tinue == 'yes':
        return ask_question()
    elif con_tinue == 'no':
        print("the program is done.")
    else:
        print("your enter is error.")

ask_question()