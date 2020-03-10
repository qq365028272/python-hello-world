#define the Initialization method, get_name() and get_total() in super class
class CartItem:
    def __init__(self, quantity, price):
        self.quantity = quantity
        self.price = price


    def get_name(self):
        return

    def get_total(self):
        total = self.quantity * self.price
        return total


#overiding method get_name() as Apple
class Apple(CartItem):  
    def get_name(self):
        return "Apple"


#overiding method get_name() as Pear
class Pear(CartItem):
    def get_name(self):
        return "Pear"
    

#Define the ShoppingCart init method, and items list (class list) , 
#define the add method, remove method, empty method and total method.
class ShoppingCart:

    items = []

    def add_to_cart(self,item):
        ShoppingCart.items.append(item)

    def remove_from_cart(self):
        ShoppingCart.items.pop()
    
    def empty_cart(self):
        ShoppingCart.items.clear()

    def cart_total(self, item, total_value=0):
        for item in ShoppingCart.items:
            total_value += item.get_total()
        return total_value


# plese enter a int number on flat_voucher,(such as 1,2,3,4...);
# plese enter a percent number with percent sign on percent_voucher,(such as 50%, 60%, 20%...);
class Voucher:
    #define the Voucher's functions : including the flat_voucher and percent_voucher, 
    #you can chiose the different of voucher when the system ask you .

    flat = None
    amount = 0

    def __init__(self,flat):
        self.flat = flat

    @classmethod
    def flat_voucher (cls):
        flat_value = float(input("enter the flat voucher: (integer) "))
        return flat_value

    @classmethod
    def percent_voucher (cls):
        percent_value = input("enter the percent voucher: (percent) ")
        aa = float(percent_value.strip('%')) 
        bb = aa/100.0 
        return bb
        
    def add_voucher(self):
        if self.flat == True:
            return Voucher.flat_voucher()
        elif self.flat == False:
            return Voucher.percent_voucher()


#This is a cyclic program, which guarantees that the program runs all the time, 
#unless it exits the program when the user enters N.

shop_cart = ShoppingCart() #Shopping cart instantiation

while True:
    ask_enter = input("pls enter the type of fruit if you want: (Apple or Pear) ")
    if ask_enter == 'Apple':#apple instantiation
        gl_quantity = int(input("Pls enter the quantity: "))
        gl_price = float(input("Pls enter the price: "))
        apple = Apple(gl_quantity,gl_price)
        shop_cart.add_to_cart(apple)

    elif ask_enter == 'Pear':#pear instantiation
        gl_quantity = int(input("Pls enter the quantity: "))
        gl_price = float(input("Pls enter the price: "))
        pear = Pear(gl_quantity,gl_price)
        shop_cart.add_to_cart(pear)

    print("--"*20)
    print("Now you have these fruit in your cart: ")
    for name in shop_cart.items:#Show all the fruit in cart
        print("Name: ",name.get_name(),"  Price: %.2f" %name.get_total())
    print("--"*20)    

    mylist = ShoppingCart.items
    myset = set(mylist)
    for item in myset:#Show quantity of each fruit now in cart
        print("the %s has found %d" %(item.get_name(),item.quantity))

#Follow the prompts for further actions
    control_enter = input("Enter Any keyboard to continue .\
        \nEnter 1. empty the cart.\nEnter 2.Show the total price in the cart:\nEnter 3. Remove a recently added fruit.")
    if control_enter == '1':
        shop_cart.empty_cart()
    elif control_enter == '2':
        print("Now the total price are : %.2f" %shop_cart.cart_total(ShoppingCart.items))
    elif control_enter == '3':
        shop_cart.remove_from_cart()

    print("--"*20) 
    print(" ")
    con_input = input("would you want to continue add? Y/N").lower()
    if con_input == 'y':
        continue
    
#Add the voucher as prompted
    pay_input = input("Would you want to use the voucher in this shopping? Y/N ").lower()
    if pay_input == 'n':
        break
    else:
        judge_flat = input("Is your voucher Flat? : Y/N ").lower()
        if judge_flat == 'y':#add the flat 
            new_voucher = Voucher(True)
            result_price = shop_cart.cart_total(ShoppingCart.items) - new_voucher.add_voucher()
            if result_price >= 0:
                print("Using voucher is successful!!! ")
                print("The Finally price is : ", result_price)
                break
            else:
                result_price = 0
                print("Using voucher is successful!!! ")
                print("The Finally price is : ", result_price)
                break
        else:
            new_voucher = Voucher(False)#add the percent 
            result_price = shop_cart.cart_total(ShoppingCart.items) * new_voucher.add_voucher()
            if result_price >= 0:
                print("Using voucher is successful!!! ")
                print("The Finally price is : ", result_price)
                break
            else:
                result_price = 0
                print("Using voucher is successful!!! ")
                print("The Finally price is : ", result_price)
                break