print("eligible to vote.")

name = input("plese type your name:")
agePerson = int ( input("plese tell us your age: "))
countryPerson = input("Plese type your country:")

if agePerson < 18 :
    print(name, " is not entitled to vote, beacuse your age is Under 18 years old.")
else:
    if countryPerson != "UK" and countryPerson != "Britain" :
        print(name, "is not entitled to vote, because your country is not Uk or Britain.")
    else :
        print(name, " is entitled to vote.")
    