f = open("demo.txt","w+")
f.write("\nI want to be in google")
f.seek(0)
data = f.read()
print(data)
f.close()

with open("demo.txt","r") as f:
    data = f.read(5)
    print(data) 
