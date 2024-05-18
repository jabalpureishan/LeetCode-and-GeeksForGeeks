from sortedcontainers import SortedList
class Solution:
    def trap(self, height: List[int]) -> int:
        prefix,suffix,p,s,n = [],[],0,0,len(height)
        for i in range(n):
            p = max(p,height[i])
            prefix.append(p)
            s = max(s,height[-(i+1)])
            suffix.append(s)
        #return prefix,suffix
        total = 0
        for i in range(n):
            total += max(0,min(prefix[i],suffix[-(i+1)])-height[i])
        return total
            