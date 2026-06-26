# 4. A person enters age. If age is greater than or equal to 18, display Eligible for voting, else display Not eligible.
class person:
    def __init__(self,x):
        self.age=int(input("enter the age:"))

    def calc(self):
        if self.age>=18:
            print("eligible for voting")
        else:
            print("Not eligible")

obj1=person(10)
obj1.calc()
