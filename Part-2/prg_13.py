# 13. A railway passenger enters age and gender. If age ≥ 60 and gender is Male, or age ≥ 58 and gender is Female, display Eligible for senior citizen concession, else display Not eligible.
class railway:
    def __init__(self,x):
        self.age=int(input("enter the age of the passenger:"))
        self.gender=input("enter the gender of the passenger:")

    def calc(self):
        if self.age>=60 and self.gender=="male" or self.age>=58 and self.gender=="female":
            print("Eligible for senior citizen concession")
        else:
            print("Not eligible")

obj1=railway(68)
obj1.calc()
