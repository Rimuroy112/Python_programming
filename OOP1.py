class student:
    name = "Rahim"
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print(self)
        print("Adding new students in class: ")

s1 = student("Karan",98)
print(s1.name,s1.marks) 

s2 = student("Arjun", 99)
print(s2.name,s2.marks) 