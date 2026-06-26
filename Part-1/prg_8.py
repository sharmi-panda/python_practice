# 8. Write a program to get the length of a square and find its area. Formula: area = side × side.
class square:
    def __init__(self,x):
        self.leng=int(input("enter the length of the square"))

    def calc(self):
        self.side=self.leng*self.leng

    def display(self):
        print("length of the square:",self.side)

obj1=square(2)
obj1.calc()
obj1.display()
