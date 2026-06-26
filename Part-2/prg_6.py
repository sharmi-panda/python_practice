# 6. A student enters marks in three subjects. If all subjects are greater than or equal to 35, display You passed, otherwise display You failed.
class mark:
    def __init__(self,x):
        self.m1=int(input("enter the 1st subject mark:"))
        self.m2=int(input("enter the 2nd subject mark:"))
        self.m3=int(input("enter the 3rd subject mark:"))

    def calc(self):
        if self.m1 and self.m2 and self.m3>=35:
            print("You passed")
        else:
            print("You failed")

obj1=mark(20)
obj1.calc()
