class student:
    college_name = "CPSCS"  # Class attributes
    # Default constructor
    def __init__(self):
        pass


    # parameterized constructor
    def __init__(self,name,marks):
        self.name = name     # Instance attributes
        self.marks = marks   # Instance attributes
    def welcome(self):
        print("Welcome student",self.name)
    def get_marks(self):
        return self.marks

s1 = student("Karan",98)
print(s1.name,s1.marks,student.college_name) 
s1.welcome()
s1.get_marks()

s2 = student("Arjun", 99)
print(s2.name,s2.marks,student.college_name) 
s2.welcome()
s2.get_marks()