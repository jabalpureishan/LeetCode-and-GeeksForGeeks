Days =int
Year1=int(input("Enter 1st Date -\nYear : "))
Month1=int(input("Month : "))
Day1=int(input("Day : "))
Year2=int(input("Enter 2nd Date -\nYear : "))
Month2=int(input("Month : "))
Day2=int(input("Day : "))
if(Year1>=Year2):
    Days=365*(Year1-Year2)
else:
    Days=365*(Year2-Year1)
if(Month1>=Month2):
    Days=Days+30*(Month1-Month2)
else:
    Days=Days+30*(Month2-Month1)
if(Day1>=Day2):
    Days=Days+(Day1-Day2)
else:
    Days=Days+(Day2-Day1)
print(Days)