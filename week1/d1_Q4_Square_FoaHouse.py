width_1 = float(input("Please input the width of first house:"))
length_1 = float(input("Please input the length of first house:"))

width_2 = float(input("Please input the width of second house:"))
length_2 = float(input("Please input the length of second house:"))

width_3 = float(input("Please input the width of third house:"))
length_3 = float(input("Please input the length of third house:"))

width_4 = float(input("Please input the width of fourth house:"))
length_4 = float(input("Please input the length of fourth house:"))

result_1 = width_1 * length_1
result_2 = width_2 * length_2
result_3 = width_3 * length_3
result_4 = width_4 * length_4

print("The first room‘s area is: ",result_1)
print("The second room‘s area is: ",result_2)
print("The third room‘s area is: ",result_3)
print("The fourth room‘s area is: ",result_4)

height_1 = float(input("Please continue input the height of first house:"))
height_2 = float(input("Please continue input the height of second house:"))
height_3 = float(input("Please continue input the height of third house:"))
height_4 = float(input("Please continue input the height of fourth house:"))

volume_1 = height_1 * result_1
volume_2 = height_2 * result_2
volume_3 = height_3 * result_3
volume_4 = height_4 * result_4

print("The first room's volume is: ",volume_1)
print("The second room's volume is: ",volume_2)
print("The third room's volume is: ",volume_3)
print("The fourth room's volume is: ",volume_4)