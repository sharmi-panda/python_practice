# 18. An ATM user enters PIN. If the entered PIN matches stored PIN, display Access Granted, else Access Denied.
class atm:
    def __init__(self,x):
        self.pin=int(input("enter the pin number"))
        self.stored=7394
    def calc(self):
        if self.pin == self.stored:
            print("Access Granted")
        else:
            print("Access Denied")

obj1=atm(20)
obj1.calc()
