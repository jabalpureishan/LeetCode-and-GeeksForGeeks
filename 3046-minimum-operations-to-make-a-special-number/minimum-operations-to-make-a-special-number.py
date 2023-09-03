"""class Solution:
    def minimumOperations(self, num: str) -> int:"""
class Solution:
    def minimumOperations(self, num: str) -> int:
        length = len(num)
        #print(len("27164518463841638493134993466318994774"))
        #print("length:",length)
        if length==1:
            if num=="0":
                return 0
            return 1
        if length<=2:
            if num in {"25","50","75","0"}:
                return 0
            elif "0" in num:
                return 1
            else:
                return 2
        else:
            Min = length
            d = {"7":[],"2":[],"5":[],"0":[]}
            for i in range(length):
                curr = num[i]
                if curr in d:
                    d[curr].append(i)
            for i in d["2"]:
                for j in d["5"]:
                    if i<j:
                        Min = min(Min,length-(i+2))
            for i in d["7"]:
                for j in d["5"]:
                    if i<j:
                        Min = min(Min,length-(i+2))
            for i in d["0"]:
                for j in d["0"]:
                    if i<j:
                        Min = min(Min,length-(i+2))
            for i in d["5"]:
                for j in d["0"]:
                    if i<j:
                        Min = min(Min,length-(i+2))
            if len(d["0"])>0:
                Min = min(Min,length-1)
            #print(d)
            #"5316527164518463841638493134993466318994774"
            return Min
                    
            
            
        