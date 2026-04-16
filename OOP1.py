class student:
    name = "Rahim"
    def __init__(self,fullname):
        self.name = fullname
        print(self)
        print("Adding new students in class: ")

s1 = student("Karan")
print(s1.name)
