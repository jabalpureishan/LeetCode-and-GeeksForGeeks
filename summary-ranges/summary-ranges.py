class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums==[]:
            return []
        if len(nums)==1:
            return [str(nums[0])]
        output = []
        #current  = nums[0]
        string = str(nums[0])
        Inf = float("inf")
        nums.append(Inf)
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1] + 1 :
                continue
            else:
                conv = str(nums[i-1])

                if string==conv:
                    res = string
                else:
                    res = string +"->"+conv
                string = str(nums[i])
                output.append(res)
        return output