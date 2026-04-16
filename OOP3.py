class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def avg(self):   # Instance method
        sum = 0;
        for val in self.marks:
            sum += val
        print("Hi",self.name,"your average marks is",sum/3)
    
    @staticmethod   # Decorator
    def c():
        print("Congratulations")

s1 = student("Arif",[98,92,95])
s1.avg()
s1.c()