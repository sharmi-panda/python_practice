# 20. Ms. Neha from ECE wants to store her role model’s name in one variable and a one‐line reason for choosing them in another variable, then display both. Write a program to help Ms. Neha.
class neha:
    def __init__(self,x):
        self.name=input("enter the role model's name")
        self.reason=input("enter the one-line reason for choosing")

    def display(self):
        self.store=(self.name,"and",self.reason)

obj1=neha('luck')
obj1.display()
