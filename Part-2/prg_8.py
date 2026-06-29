# 8. A person types a character. If it is a vowel, display Vowel, otherwise display Consonant.
class cha:
    def __init__(self,x):
        self.name=input("enter a letter")

    def calc(self):
        if self.name =='a' or 'e' or 'i' or 'o' or'u':
            print("vowel")
        else:
            print("constant")

obj1=cha(20)
obj1.calc()
