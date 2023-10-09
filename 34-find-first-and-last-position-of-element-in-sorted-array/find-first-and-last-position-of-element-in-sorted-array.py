class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        Output = []
        length = len(nums)
        if target not in nums:
            Output = [-1,-1]
            return(Output)
        else:
            for i in range(length):
                if(nums[i]==target):
                    Output.append(i)
                    break
            for i in range(1,length+1):
                i = -i
                if(nums[i]==target):
                    Output.append(length+i)
                    break
            return(Output)