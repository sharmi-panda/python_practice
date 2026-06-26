# 10. Write a program to get the cost of a pen and notebook. Find and display the total cost.
class stationary:
    def __init__(self,x):
        self.pen=int(input("enter the cost of the pen"))
        self.notebook=int(input("enter the cost of the notebook"))
        
    def calc(self):
        self.total=self.pen+self.notebook

    def display(self):
        print("The total cost:",self.total)

obj1=stationary(29)
obj1.calc()
obj1.display()
