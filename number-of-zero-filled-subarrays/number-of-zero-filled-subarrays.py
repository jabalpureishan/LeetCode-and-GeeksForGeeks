class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        output = 0
        count = 0
        nums.append(1)
        for i in nums:
            if i==0:
                count += 1
            else:
                output += (count*(count + 1))//2
                count = 0
        return output