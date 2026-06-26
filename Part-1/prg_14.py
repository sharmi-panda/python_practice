# 14. Write a program to get the base and height of a triangle and find its area. Formula: area = (base × height) / 2.
class triangle:
    def __init__(self,x):
        self.base=float(input("enter the base of the triangle:"))
        self.height=float(input("enter the height of the triangle:"))

    def calc(self):
        self.area=(self.base*self.height)/2
        print("Area of the triangle:",self.area)

obj1=triangle(20)
obj1.calc()
