# 2. write a program to find the perimeter of a rectangle. Formula:perimeter=2*(length+width)
class peri:
    def __init__(self,x):
        self.length=float(input("enter the length"))
        self.width=float(input("enter the width"))

    def cal(self):
        self.calc=2*(self.length+self.width)

    def display(self):
        print(self.calc)

obj1=peri(4)
obj1.cal()
obj1.display()
