length = int(input(""))
arr = list(map(int, input("").split()))
First = arr[0]
result,count = 0,0
def Update(count):
    if(count>result):
        result = count
for i in range(1,length):
    if(First>=arr[i]):
        count+=1
        First = arr[i]
    else:
        Update(count)
        First = arr[i]
        break        
else:
    count = 0
    First = arr[i]
print(result)

