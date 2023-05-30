I=str(input())
string=""
for i in range(1,len(I)+1):
  i=-i
  string=string+I[i]
if(string==I):
    print(True)
else:
    print(False)
