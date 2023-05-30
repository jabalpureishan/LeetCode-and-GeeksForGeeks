Word = str(input("Enter String : "))
Check =str(input("Enter letter to check : "))
count = 0
for i in Word :
    count=count +1
print("length of string : ", count)
print("Length Check = ",len(Word))
if Check in Word:
    print("present")
else:
    print("Absent")

