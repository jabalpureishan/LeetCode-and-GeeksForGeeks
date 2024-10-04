class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        ans = 0
        skill.sort()
        for i in range(len(skill)//2):
            if skill[i]+skill[-(i+1)]!=skill[0]+skill[-1]:
                return -1
            ans += skill[i]*skill[-(i+1)]   
        return ans
        