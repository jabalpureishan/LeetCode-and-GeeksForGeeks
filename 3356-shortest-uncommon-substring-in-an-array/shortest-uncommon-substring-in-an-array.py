class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        n = len(arr)
        ans = []
        for i in range(n):
            l = len(arr[i])
            Min = l*"~"
            for j in range(l):
                for k in range(j+1,l+1):
                    curr = arr[i][j:k]
                    for h in range(n):
                        if h!=i and curr in arr[h]:
                            break
                    else:
                        #print("curr not found",curr)
                        if len(curr)<len(Min):
                            Min = curr
                        elif len(curr)==len(Min):
                            #print("compare",Min,curr)
                            Min = min(Min,curr)
                            #print("Res:",Min)
            if Min==l*"~":
                Min = ""
            ans.append(Min)
        return ans
        