length = int(input(""))
Arr = list(map(int, input("").split()))
Arr.sort(reverse = True)
Arr.append(0)
for i in range(length+1):
    if(sum(Arr[:i+1])>sum(Arr[i+1:])):
        print(i+1)
        break
    else:
        continue