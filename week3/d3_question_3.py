from datafile import data

def list_print_all(data_list):
    i = 0
    while i <= len(data_list)-1:
        print("name: ",data_list[i], "  grade: ",data_list[i+1], end ="  ")
        if data_list[i+1] >= 70:
            print("State: Distinction")
        elif 60 <= data_list[i+1] < 70:
            print("State: Merit")
        elif 40 <= data_list[i+1] < 60:
            print("State: Pass")
        else:
            print("State: Fail")
        i = i+2

def list_print_re(data_list):
    i = 0
    while i <= len(data_list)-1:
        if 30 <= data_list[i+1] < 40:
            print("name: ",data_list[i], "  grade: ",data_list[i+1], end ="  ")
            print("State: Fail")
            print("You are entitled to a resubmission! ")
        i = i+2

def list_print_3(data_list):
    i = 0
    sum = 0
    n = 0
    while i <= len(data_list)-1:
        sum = sum + data_list[i+1]
        if data_list[i+1] == 95:
            print("High mark:  ",data_list[i], "   ",data_list[i+1])
        elif data_list[i+1] == 4:
            print("Marks range:  ", data_list[i+1]," ~ 95")
        i = i+2
        n += 1
    average = sum / n
    print(average)
    return average


def list_print_4():
    new_data = data[1:len(data):2]
    a = 0
    m = 0
    p = 0
    q = 0
    while a < len(new_data):
        if new_data[a] >= 40:
            m = m + 1
        if new_data[a] < 47.24:
            p = p + 1
        if new_data[a] < 40:
            q = q + 1
        a += 1
    print(m,"students higher than average. ", p, "stdudents lower than average. ", q, "students are fail.")

list_print_all(data)
print("---------------------------------------")
list_print_re(data)
print("---------------------------------------")
list_print_3(data)
print("---------------------------------------")
list_print_4()

