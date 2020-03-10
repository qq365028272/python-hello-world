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
        ShoppingCart.items = []

    def cart_total(self, item, total_value=0):
        for item in ShoppingCart.items:
            total_value += item.get_total()
        return total_value

#This is a cyclic program, which guarantees that the program runs all the time, 
#unless it exits the program when the user enters N.

shop_cart = ShoppingCart()

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
        print("Name: ",name.get_name(),"  Price: ",name.get_total())
    print("--"*20)    

    mylist = ShoppingCart.items
    myset = set(mylist)
    for item in myset:#Show quantity of each fruit now in cart
        print("the %s has found %d" %(item.get_name(),item.quantity))

    print(" ")
#Follow the prompts for further actions
    control_enter = input("Return continue add fruit.\nEnter 1. empty the cart.\nEnter 2.total price in the cart:\nEnter 3. remove the recently a fruit in your cart.")
    if control_enter == '1':
        shop_cart.empty_cart()
    elif control_enter == '2':
        print("Now the total price are : %.2f" %shop_cart.cart_total(ShoppingCart.items))
    elif control_enter == '3':
        shop_cart.remove_from_cart()

    print("--"*20) 
    print(" ")
    con_input = input("would you want to continue? Y/N").lower()
    if con_input == 'n':
        break
