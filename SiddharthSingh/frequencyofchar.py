
String=input("Enter String : ")
vowels,consonant,number,space_count=[],[],[],0
for i in String:
    if((ord(i)>=48) and (ord(i)<=57)):
        i=int(i)
        if i not in number:
            number.append(i)
    if((i=="a") or (i=="o") or (i=="e") or (i=="i") or (i=="u")):
        if i not in vowels:
            vowels.append(i)
    else:

        if i not in consonant:
            consonant.append(i)
    if(i==" "):
        space_count=space_count+1
print("vowels : ",len(vowels))
print("consonant : ",len(consonant))
print("number : ",len(number))
print("spaces : ",space_count)

