class Greeter:
    name = " "

    def __init__(self, name):
        self.name = name
    
    def greet_to_screen(self):
        print("Hello %s" %self.name)

    def greet_to_file(self):
        with open("hi.txt", mode="w") as hi_text:
            hi_text.write("Hello %s" %self.name)

greeter =Greeter(input("pls enter a nmae : "))
# enter any name, such as Fred, Jackson ....

greeter.greet_to_screen()

greeter.greet_to_file()
