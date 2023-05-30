class Solution:
    def stringFilter(str):
        length = len(str)
        out = ""
        for i in range(length-1):
            #print("i:",i,"str[i]",str[i])
            if str[i]=="b":
                continue
            elif str[i]=="a" and str[i+1]=="c":
                continue
            elif str[i]=="c" and str[i-1]=="a":
                continue
            else:
                out += str[i]
                #print("out update:",out)
        if str[-2:]!="ac" and str[-1]!="b":
            out += str[-1]
        return out

    print(stringFilter("aacbacc"))
    print(stringFilter("aacb"))
    print(stringFilter("aca"))
