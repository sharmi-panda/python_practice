# 3. A user enters a number. If it is even, display Even number, otherwise Odd number.
class user:
    def __init__(self,x):
        self.nu=int(input("enter the number:"))

    def cal(self):
        if self.nu%2==0:
            print("even number")
        else:
            print("odd number")

obj1=user(10)
obj1.cal()
