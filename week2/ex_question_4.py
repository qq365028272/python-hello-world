first_num = int(input("please input the first number: "))
second_num = int(input("please input the second number: "))
third_num = int(input("please input the third number: "))

if first_num > second_num:
    if second_num >third_num:
        print(third_num,"  ", second_num,"  ",first_num )
    elif third_num > first_num:
        print(second_num, "  ", first_num, "  ", third_num)
    else:
        print(second_num,"  ", third_num, "  ",first_num )
elif first_num < second_num:
    if second_num < third_num:
        print(first_num, "  ", second_num, "  ", third_num)
    elif third_num < first_num:
        print(third_num, "  ",first_num, "  ", second_num)
    else:
        print(first_num, "  ",third_num,"  ",second_num )