def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

askMark = input("please type your mark: ")

if is_number(askMark) == True:
    askMark = int(askMark)
    if askMark >= 0 and askMark <= 100:
        if askMark == 0:
            print("Grade : N/S")
        elif askMark >=1 and askMark <=39 :
            print("Grade : F")
        elif askMark >= 40 and askMark <= 49:
            print("Grade : D")
        elif askMark >= 50 and askMark <= 59:
            print("Grade : C")
        elif askMark >= 60 and askMark <= 69:
            print("Garde : B")
        elif askMark >= 70 and askMark <= 79:
            print("Grade : A")
        else:
            print("Gadre : A*")
    elif askMark < 0 :
        print("the number is negative.")
    else:
        print("the number is greater than 100.")
else:
    print("it dosen't a number.")