old_numb = input("type your first number: ")

new_type = input("Plese input your second number: ")

while (new_type != "quit") and (old_numb != "quit"):
    try:
        old_numb = int(old_numb)
        new_type = int(new_type)
        if old_numb > new_type:
            print("Now these are have :\nOld number: ",old_numb,"\nNew number",new_type,"\n",old_numb,"is biggest number.")
        elif old_numb < new_type:
            print("Now these are have :\nOld number: ",old_numb,"\nNew number",new_type,"\n",new_type,"is biggest number.")
        else:
            print("Now these are have :\nOld number: ",old_numb,"\nNew number","\n",new_type,"both nunmber are same.")
        old_numb = input("Plese input your NEW first number: ")
        new_type = input("Plese input your NEW second number: ")
    except :
        print("This order is error.")
        break
print("Program is quit.")