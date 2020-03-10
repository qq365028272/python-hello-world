#This program is to make decisions on loan applications.

credit=int(input("Please input your Credt score from 0 to 10"))
address=int(input("Please input your months at preset address" ))
income=input("Please input your income £s")
request=input("Please input your loan amount requested £s")

if income==0 or credit==0 or address<12:
    print("Sorry, your loan request has been refued")

elif request>income:
    if request>income and request<income*2 and address>=60 and credit>=5:
        print("Congradulation! Your loan request has been granted")
    else:
        print("Sorry Your loan request has been refused")

elif request<income:
    if 7<=credit<=10 and 12<address<60:
        print("Congradulation! Your loan request has been granted")
    elif 2<=credit<=5 and address>=60:
        print("Congradulation! Your loan request has been granted")
    elif credit==1 and address>=12 and request<income*0.2:
        print("Congradulation! Your loan request has been granted")
    else:
        print("Sorry Your loan request has been refused")
   
else:
    print("Sorry Your loan request has been refused")
    
    