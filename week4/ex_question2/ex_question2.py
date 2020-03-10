def Sear_name (cus_value):
    new_lst = []
    with open ("menu.txt", mode = "r") as The_menu:
        for line in The_menu:
            line = line.rstrip("\n")
            new_lst.append(line.lower())    
    n = 0
    for i in new_lst:
        cus_value = cus_value.lower()
        if cus_value in i:
            print(i)
            n += 1
        else:
            continue    
    if n == 0:
        print("Sorry, we don't have ", cus_value,"in our restaurant.")
            

ask_name = input("Which sandwich of type do you like? ")

Sear_name(ask_name)

# print("Thank your choise",ask_value,". We will arrange the serving as soon as possible.")