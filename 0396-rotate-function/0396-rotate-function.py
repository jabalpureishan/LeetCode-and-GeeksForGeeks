class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        new = [nums[-1]]
        new.extend(nums)
        #print("new:",new)
        length = len(nums)
        if length==1:
            return 0
        Sum = sum(nums[:length-1])
        #print("Sum:",Sum)
        SLIndex = length - 1
        #print("SLIndex:",SLIndex)
        last = nums[-1]

        s_last = nums[-2]
        #print("last:",last,"s_last:",s_last)

        Initial = 0
        for i in range(length):
            Initial += i*nums[i]
        Max = Initial
        #print("Initial:",Initial)
        #print("******************")        
        for i in range(length-1):
            Initial -= last*(length-1)
            Initial += Sum
            #print("Initial:",Initial)
            if Initial>Max:
                #print("Max Update")
                Max = Initial
            Sum += last
            Sum -= s_last
            last = s_last
            SLIndex -= 1
            s_last = new[SLIndex]
            #print("Sum:",Sum,"last:",last,"s_last:",s_last)
        return Max
