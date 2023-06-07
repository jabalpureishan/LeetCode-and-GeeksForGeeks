class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a,b,c = str(bin(a))[2:],str(bin(b))[2:],str(bin(c))[2:]
        lena,lenb,lenc = len(a),len(b),len(c)
        Max = max(lena,lenb,lenc)
        if Max==lena:
            b = "0"*(lena-lenb) + b
            c = "0"*(lena-lenc) + c
        elif Max==lenb:
            a = "0"*(lenb-lena) + a
            c = "0"*(lenb-lenc) + c
        elif Max==lenc:
            b = "0"*(lenc-lenb) + b
            a = "0"*(lenc-lena) + a
        #print("a:",a,"b:",b,"c:",c)
        count = 0
        for i in range(-1,-(Max+1),-1):
            #print("i:",i)
            if c[i]=="1":
                #print("c[i]==1")
                if (int(a[i])|int(b[i]))==1:
                    #print("no change")
                    continue
                else:
                    #print("change one to 1")
                    count += 1
            elif c[i]=="0":
                #print("c[i]==0")
                if ((int(a[i])|int(b[i]))==0):
                    #print("no change")
                    continue
                elif(a[i]=="1" and b[i]=="1"):
                    #print("both 1 so 2 change")
                    count += 2
                else:
                    #print("either is 1 so 1 change")
                    count += 1
            
        return count