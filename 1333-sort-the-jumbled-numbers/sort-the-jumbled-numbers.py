from collections import OrderedDict
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        main,hmap,final = {},{},[]
        for i in nums:
            hmap[i] =hmap.get(i,0) + 1
        for i in nums:
            curr,ans = str(i),""
            for j in curr:
                ans += str(mapping[int(j)])
            main[i] = int(ans)
        main = sorted(main.items(),key=lambda x:x[1])
        for i in main:
            final.extend([i[0]]*hmap[i[0]])
            hmap[i[0]] -= 1
        return final