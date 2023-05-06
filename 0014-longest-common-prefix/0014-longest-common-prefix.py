class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        Min = len(strs[0])
        n = len(strs)
        for i in range(1,n):
            Min = min(Min,len(strs[i]))
        #print("Min:",Min)
        output = ""
        for i in range(Min):
            pick = strs[0][i]
            #print("pick:",pick)
            for j in range(1,n):
                #print("check:",strs[j][i])
                if strs[j][i]!=pick:
                    #print("break executed")
                    return output
            else:
                output += pick
                #print("break not executed output:",output)
        return output