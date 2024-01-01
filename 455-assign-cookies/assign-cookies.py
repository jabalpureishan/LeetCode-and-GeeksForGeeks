class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        lens,count = len(s),0
        g.sort()
        s.sort()
        ind = 0
        for i in g:
            for j in range(ind,lens):
                if s[j]>=i:
                    count += 1
                    ind = j+1
                    break
        return count
            

            
            