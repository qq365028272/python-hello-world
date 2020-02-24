#This program is to make decisions on loan applications.

credit_Score = int(input("Your Credit score (0 to 10 inclusive): "))
address_term = int(input("Address term (months at present address): "))
income = int(input("How many your income (£s) per year? "))
request = int(input("Request (£s) (loan amount requested): "))

if (income == 0) or (credit_Score == 0) or (address_term < 12) :
    print("The request is refused.")
elif request > income:
    if request < income * 2 and address_term >= 60 and credit_Score > 5 :
        print("The loan is  granted!")
    else:
        print("The request is refused.")
elif (7 <= credit_Score <= 10) and (12 < address_term < 60) and (request < income):
    print("The loan is  granted!")
elif 2 <= credit_Score <= 5 and address_term >= 60 and request < income :
    print("The loan is  granted!")
elif credit_Score == 1 and address_term > 12 and request < income * 0.2:
    print("The loan is  granted!")
else:
    print("The request is refused.")