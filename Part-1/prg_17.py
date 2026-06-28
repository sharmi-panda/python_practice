# 17. Mr. Rahul from EEE wants to keep the name of his favorite book in one variable and the author’s name in another variable, then display both. Write a program to help Mr. Rahul.
class rahul:
    def __init__(self,x):
        self.book=input("enter the favorite book:")
        self.author=input("enter the author name:")

    def display(self):
        print(self.book,"by author",self.author)

obj1=rahul('EEE')
obj1.display()
    
