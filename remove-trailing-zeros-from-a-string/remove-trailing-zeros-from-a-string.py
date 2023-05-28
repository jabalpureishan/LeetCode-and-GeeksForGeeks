class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        length = len(num)
        count  = 0
        for i in range(-1,-length,-1):
            if num[i]=="0":
                count += 1
            else:
                break
        #print("count:",count)
        num = num[:length-count]
        return num
            
        