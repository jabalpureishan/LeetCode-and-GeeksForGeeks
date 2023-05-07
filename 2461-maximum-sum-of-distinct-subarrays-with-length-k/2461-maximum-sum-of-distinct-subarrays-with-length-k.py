class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        length  = len(nums)
        window = k
        slides = length - window 
        Max = 0
        d = {}
        Sum = 0
        for i in nums[:k]:
            Sum += i
            d[i] = d.get(i,0) + 1
        #print("D:",d)
        #print("Sum:",Sum)
        if len(d)==k:
            Max = max(Max,Sum)
        for i in range(slides):
            Add = nums[window]
            Sub = nums[i]
            #print("Add:",Add,"Subtract:",Sub,"curr Sum:",Sum)
            Sum = Sum + Add - Sub
            #print("Sum after:",Sum)
            d[Add] = d.get(Add,0) + 1
            d[Sub] -= 1
            if d.get(Sub)==0:
                d.pop(Sub)
            if len(d)==k:
                Max = max(Max,Sum)
            window += 1
        return Max
