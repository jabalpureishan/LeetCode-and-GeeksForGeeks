String=input("Enter a String : ")
alphabets=[]
A=""
for i in range(97,123):
  alphabets.append(chr(i))
for j in String:
  if j in alphabets:
    A=A+j
  else:
    pass
print(A)

