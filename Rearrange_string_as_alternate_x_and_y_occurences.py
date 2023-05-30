class Solution:
    def rearrange(X,Y,S):
        out = ""
        numx,numy = 0,0
        for i in S:
            if i=="0":
                numx += 1
            else:
                numy += 1
        while(numx>0 and numy>0):
            out += "0"*X
            numx -= X
            out += "1"*Y
            numy -= Y
        if numx==0:
            out += numy*"1"
        else:
            out += nums*"0"
        return out

    print(rearrange(1,1,"0011"))
    print(rearrange(1,1,"1011011"))