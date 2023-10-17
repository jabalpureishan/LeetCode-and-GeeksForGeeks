class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix,suffix,Sum,ans,length = [],[],1,[],len(nums)
        for i in nums:
            Sum *= i
            prefix.append(Sum)
        Sum = 1
        for i in range(-1,-(length+1),-1):
            Sum *= nums[i]
            suffix.append(Sum)
        suffix = suffix[::-1]
        print(prefix,suffix)
        for i in range(length):
            if i==0:
                ans.append(suffix[i+1])
            elif i==length-1:
                ans.append(prefix[i-1])
            else:
                ans.append(prefix[i-1]*suffix[i+1])
        return ans               