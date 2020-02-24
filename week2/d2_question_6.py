type_ask = input("plese type of the Porkmon type,This can be one of:\na. Fire\nb. Water\nc. Grass\nd. Electric\nInput: ")

name_ask = input("What's the first letter of Pokemon's name?\nYou can type the first name which are one of the below Words:\nS T C M B O P V\nInput: ")

S_name = "Squirtle"
T_name = "Tentacool"
C_name = "Charmander"
M_name = "Moltres"
B_name = "Bulbasaur"
O_name = "Oddish"
P_name = "Pikachu"
V_name = "Voltorb"

if (type_ask == "b") or (type_ask == "Water"):
    if name_ask == "S":
        print("This Pokemon is ",S_name)
    elif name_ask == "T":
        print("This Pokemon is ",T_name)
    else:
        print("There is no Pokemon from this name.")

elif (type_ask == "a") or (type_ask == "Fire"):
    if name_ask == "C":
            print("This Pokemon is ",C_name)
    elif name_ask == "M":
        print("This Pokemon is ",M_name)
    else:
        print("There is no Pokemon from this name.")

elif (type_ask == "c") or (type_ask == "Grass"):
    if name_ask == "B":
            print("This Pokemon is ",B_name)
    elif name_ask == "O":
        print("This Pokemon is ",O_name)
    else:
        print("There is no Pokemon from this name.")

elif (type_ask == "d") or (type_ask == "Electric"):
    if name_ask == "P":
            print("This Pokemon is ",P_name)
    elif name_ask == "V":
        print("This Pokemon is ",V_name)
    else:
        print("There is no Pokemon from this name.")
