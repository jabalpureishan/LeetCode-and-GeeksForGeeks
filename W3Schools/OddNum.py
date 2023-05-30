print_from=int(input("Print Odd No's from : "))
print_to=int(input("To :"))
if(print_from%2==0):
    print_from=print_from+1
    print_to=print_to+1
    for i in range(print_from,print_to,2):
        print(i,end=",")
else:
    print_to=print_to+1
    for i in range(print_from,print_to,2):
        print(i,end=",")
