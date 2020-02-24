buffer = []
i = 0

with open ("/Users/bohengwang/Desktop/VSCODEPROJECT/day4/output.txt", "r") as file :
    for line in file :
        buffer += [line]
        if i == 2:
            buffer +=["python"]
        i += 1

with open ("/Users/bohengwang/Desktop/VSCODEPROJECT/day4/output2.txt", "w") as file :
    for item in buffer :
        file.write(item + "\n")