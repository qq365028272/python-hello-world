def ask_question ():
    x = float(input("pls input a number x: "))
    y = float(input("pls input a number y: "))
    enter_int = int(input("pls input 1(to add), 2(to subtract),3(to multiply) or 4(to divide)"))
    if enter_int == 1:
        print(x+y)
    elif enter_int == 2:
        print(x-y)
    elif enter_int == 3:
        print(x*y)
    elif enter_int == 4:
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
