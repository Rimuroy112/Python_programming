class student:
    def __init__(self, phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math
    
    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3) + "%"

s1 = student(98,97,99)
print(s1.percentage)

s1.phy = 88
print(s1.percentage)
