class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos,neg = [],[]
        for i in nums:
            if i>0:
                pos.append(i)
            else:
                neg.append(i)
        ind = 0
        for i in range(0,len(nums),2):
            nums[i] = pos[ind]
            nums[i+1] = neg[ind]
            ind += 1
        return nums
        