# 1. write a program to get two numbers, multiply them, and display the result
class Calc:
    def __init__(self,x):
        self.a=int(input("enter the 1st number:"))
        self.b=int(input("enter the 2nd number:"))

    def cal(self):
        self.mul=self.a*self.b

    def display(self):
        print(self.mul)
        
obj1=Calc(5)
obj1.cal()
obj1.display()
