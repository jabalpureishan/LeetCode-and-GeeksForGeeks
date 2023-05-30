A,B=input("Enter two numbers : ").split()
A,B=int(A),int(B)
if(A>B):
    G=A
elif(B>=A):
    G=B
HCF_A,HCF_B,HCF=[],[],[]
for i in range(1,G+1):
  HCF_A.append(A*i)
  HCF_B.append(B*i)
for j in HCF_A:
    if j in HCF_B:
        HCF.append(j)
    else:
        pass
print(min(HCF))

  