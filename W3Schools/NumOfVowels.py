word=str(input(""))
count=0
for i in word:
    if(i=="a" or i=="e" or i=="i" or i=="u" or i=="o"):
        count=count+1
print(count)