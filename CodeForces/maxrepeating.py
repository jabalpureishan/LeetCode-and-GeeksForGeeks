I = str(input(""))
length = len(I)
count = 0
answer = I[0]
final = 1
for i in range(length):
	if (i < length - 1 and
		I[i] == I[i + 1]):
		final += 1
	else:
		if final > count:
			count = final
			answer = I[i]
		final = 1
if(count>=7):
    print("YES")
else:
    print("NO")
	


