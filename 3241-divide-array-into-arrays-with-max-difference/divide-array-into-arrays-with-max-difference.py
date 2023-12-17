class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(0,len(nums),3):
            curr = nums[i:i+3]
            #print("curr:",curr)
            if curr[-1]-curr[-3]<=k:
                ans.append(curr)
            else:
                return []
        return ans

        