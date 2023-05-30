Dec = int(input("Enter Decimal : "))
Format=int(input("Enter Bits 4/8 : "))
a= 0
while(Format>0):
    if(Dec>Format):
        a = a+1
        Dec = Dec - Format
        print(a, end= "")
