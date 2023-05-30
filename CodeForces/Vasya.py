n,m = input().split()
n,m = int(n),int(m)
count = 0
while(n>0):
    count = count + 1
    n = n - 1
    if((count%m)==0):
        n = n + 1
print(count)        
