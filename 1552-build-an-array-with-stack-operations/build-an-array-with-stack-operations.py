class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans,ptr,i,lena = [],0,1,len(target)
        while i<=n and ptr<lena:
            if target[ptr]==i:
                ans.append("Push")
                ptr += 1
            else:
                ans.extend(["Push","Pop"])
            i += 1
        return ans
        