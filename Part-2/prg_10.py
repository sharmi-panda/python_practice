# 10. For a given mobile number, check: if the last digit is divisible by 3, display Lucky number, otherwise display Unlucky number.
class number:
    def __init__(self,x):
        self.mobile=input("enter the mobile number:")

    def calc(self):
        self.last=int(self.mobile[-1])
        if self.last %3==0:
            print("lucky number")
        else:
            print("unlucky number")

obj1=number(20)
obj1.calc()
