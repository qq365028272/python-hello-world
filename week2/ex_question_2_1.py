print("eligible to vote.")

name = input("plese type your name:")
agePerson = int ( input("plese tell us your age: "))
if agePerson < 18 :
    print(name, " is entitled to vote, beacuse your age is Under 18 years old.")
else:
    countryPerson = input("Plese type your country:")
    if countryPerson == "UK" or countryPerson == "Britain" :
        print(name, " is entitled to vote.")
    else :
        print(name, " is not entitled to vote.")
    
