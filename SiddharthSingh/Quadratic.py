import math
a = float(input("Enter Coefficient in the Form ax^2 + bx + c = 0 \na :" ))
b = float(input("b : "))
c = float(input("c : "))
print("1st Root", (-b + math.sqrt(b*b - 4*a*c))/2*a )
print("2nd Root", (-b - math.sqrt(b*b - 4*a*c))/2*a )
print(id(a))