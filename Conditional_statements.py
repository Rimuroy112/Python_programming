number = int(input("Number: "))
if(number > 80):
    print("A")
elif(number > 70):
    print("B")
else:
    print("C")

food = input("Food: ")
eat = "Yes" if food == "cake" else "NO"
print(eat)

print("sweet") if food == "cake" or food == "jalebi" else print("Not sweet")

age = int(input("Age: "))
vote = ("No","Yes")[age >= 18]
print(vote)