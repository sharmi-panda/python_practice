# 16. Ms. Priya from CSE wants to store her three favorite foods in one variable and display them. Write a program to help Ms. Priya.
class priya:
    def __init__(self,x):
        self.food1=input("enter the 1st favorite food:")
        self.food2=input("enter the 2nd favorite food:")
        self.food3=input("enter the 3rd favorite food:")

    def calc(self):
        self.food=[self.food1,self.food2,self.food3]
        print("Three favorite foods are:",self.food)

obj1=priya(15)
obj1.calc()
