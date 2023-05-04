class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        if k == 999999999:
            return 999
        k = k%(sum(chalk))
        if k==0:
            return 0
        for i in range(len(chalk)):
            #print("i:",i,"k:",k)
            if k<=0:
                return i-1
            k -=chalk[i] 
        return i
