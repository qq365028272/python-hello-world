askNumb = int(input("please tell me a integer number: "))

if askNumb % 3 == 0 and askNumb % 5 != 0:
    print("Fizz")
elif askNumb % 5 ==0 and askNumb % 3 !=0:
    print("Buzz")
elif (askNumb % 3 or askNumb % 5) == 0:
    print("Fizz Buzz")
else:
    print(askNumb)