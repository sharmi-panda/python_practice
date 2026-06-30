# 15. A student enters roll number. If roll number is divisible by 2, assign Lab Group A, else assign Lab Group B.
class student:
    def __init__(self,x):
        self.roll=int(input("enter the roll number:"))

    def calc(self):
        if self.roll%2==0:
            print("lab group A")
        else:
            print("lab group B")

obj1=student(1)
obj1.calc()
