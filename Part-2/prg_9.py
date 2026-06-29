# 9. A bank asks to enter account balance. If balance is less than 1000, display Low balance warning, else display Sufficient balance.
class bank:
    def __init__(self,x):
        self.amount=int(input("enter the account balance:"))

    def calc(self):
        if self.amount<=1000:
            print("low balance warning")
        else:
            print("sufficient balance")

obj1=bank(56)
obj1.calc()
