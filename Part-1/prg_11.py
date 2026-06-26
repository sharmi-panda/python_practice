# 11. Write a program to get the radius of a sphere and find its volume. Formula: V = (4/3) × 3.14 × r3.
class sphere:
    def __init__(self,x):
        self.radius=float(input("enter the radius of the sphere:"))

    def calc(self):
        self.volume=((4/3)*3.14*(self.radius**3))
        print("Volume of the sphere:",self.volume)

obj1=sphere(2)
