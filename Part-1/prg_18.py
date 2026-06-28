# 18. Ms. Anjali from IT wants to record the title of her favorite song and a short description of it in a single variable. Write a program to help Ms. Anjali.
class anjali:
    def __init__(self,x):
        self.title=input("enter the title of your favorite song")
        self.description=input("enter the short description of the song")

    def display(self):
        self.song=[self.title,self.description]
        print("Title of her favorite song and description:",self.song)

obj1=anjali("dog")
obj1.display()        
