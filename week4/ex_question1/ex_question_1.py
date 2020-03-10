def Sear_name (cus_value):
    with open ("menu.txt", mode = "r") as The_menu:
        for line in The_menu:
            if cus_value in line:
                return 1
            else:
                return 0

ask_value = input("Which sandwich of type do you like? ")

result = Sear_name(ask_value)

if result == 1:
    print("Thank your choise",ask_value,". We will arrange the serving as soon as possible.")
elif result == 0:
    print("Sorry, we don't have ", ask_value,"in our restaurant.")
