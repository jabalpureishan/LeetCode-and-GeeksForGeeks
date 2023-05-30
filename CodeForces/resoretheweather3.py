t=int(input())
for _ in range(t):
  n,k=map(int,input().split())
  a=list(map(int,input().split()))
  b=list(map(int,input().split()))
  print("a:",a)
  print("b:",b)
  a=[(a[i],i) for i in range(n)]
  print("new a",a)  
  a.sort()
  b.sort()
  print("sorted a:",a)
  print("sorted b:",b)
  o=[0]*n
  for i in range(n):
    v,j=a[i]
    print("v:",v,"j:",j,"a[i]",a[i])
    o[j]=b[i]
    print("o[j]",o[j])
  print(*o)