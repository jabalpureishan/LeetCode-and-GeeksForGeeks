class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        done,lens,count = set(),len(s),0
        g.sort()
        s.sort()
        for i in g:
            for j in range(len(s)):
                if j not in done:
                    if s[j]>=i:
                        count += 1
                        done.add(j)
                        break
            if len(done)>=len(g):
                break
        return count
            

            
            
