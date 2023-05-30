a=int(input("Enter a : "))
b=int(input("Enter b : "))
print(id(a))
print(id(b))
if(a is not b):
    print("Different")
else:
    print("Same")

