# 15. Write a program to get the number of students in a class and number of apples. Find how many apples each student gets and how many are left.
class donate:
    def __init__(self,x):
        self.student=int(input("enter the no. of student"))
        self.apple=int(input("enter the no. of apples"))

    def calc(self):
        self.given=self.apple//self.student
        self.left=self.apple%self.student
        print("apple each student gets:",self.given)
        print("apple left:",self.left)

obj1=donate(7)
obj1.calc()
