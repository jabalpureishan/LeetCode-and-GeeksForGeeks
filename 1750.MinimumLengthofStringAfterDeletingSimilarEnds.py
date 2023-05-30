def minimumLength(s):
    length = len(s)
    current = s[0]
    front = -1
    back = 0
    change = True
    while change:
        front = -1
        back = 0
        if s!="":
            if s[0]!=s[-1]:
                change = False
                break
            for i in range(length):
                if s[i]==current:
                    front += 1
                else:
                    break
            for i in range(-1,-(length+1),-1):
                if s[i]==current:
                    back -= 1
                else:
                    break
            #print("front:",s[:front+1],"back:",s[back:])
            s = s[front+1:back] #+ s[:back]
            #print("s:",s)
            if s!="":
                current = s[0]
                #print("new current",current)
            #print("-------------")
    return len(s)
                
minimumLength("aabccabba")
