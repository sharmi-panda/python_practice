# 19. Mr. Karthik from MECH has three dream travel destinations and wants to store them in one variable and display them. Write a program to help Mr. Karthik.
class karthik:
    def __init__(self,x):
        self.dream1=input("enter the 1st dream travel destination:")
        self.dream2=input("enter the 2nd dream travel destination:")
        self.dream3=input("enter the 3rd dream travel destination:")

    def display(self):
        self.travel=[self.dream1,self.dream2,self.dream3]
        print("Three dream travel destination:",self.travel)

obj1=karthik("apple")
obj1.display()
