class MathEngine:

    def __init__(self,numb):
        self.numb = numb
    
    def add(self, add_num):
        self.numb += add_num
        return self.numb
    
    def sub(self, sub_num):
        self.numb -= sub_num
        return self.numb
    
    def mult(self, mult_num):
        self.numb *= mult_num
        return self.numb
    
    def div(self, div_num):
        self.numb /= div_num
        return self.numb


while True:
    new_math_numb = MathEngine(int(input("pls enter a numb: ")))

    print('if you want to add, subtract, multiply and divide this numb,\
        pls enter 1(add), 2(sub) , 3(mult), 4(div) : ')

    control_order = input(" ")

    if control_order == '1':
        new_math_numb.add(int(input("pls enter your number :")))
        print(new_math_numb.numb)
    elif control_order == '2':
        new_math_numb.sub(int(input("pls enter your number :")))
        print(new_math_numb.numb)
    elif control_order == '3':
        new_math_numb.mult(int(input("pls enter your number :")))
        print(new_math_numb.numb)
    elif control_order == '4':
        new_math_numb.div(int(input("pls enter your number :")))
        print(new_math_numb.numb)
    
    action_str = input(" if You want to EXIT,  pls enter exit :").lower()

    if action_str == 'exit':
        break
