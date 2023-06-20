class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k==0:
            return nums
        out = []
        length = len(nums)
        divide = k*2 + 1
        if divide<=length:
            Sum =  sum(nums[:divide])
        else:
            Sum = 0
        #print("Sum:",Sum)
        for i in range(length):
            #Sum += nums[i]
            if i<k or i>=(length-k):
                out.append(-1)
            else:
                #print("i:",i,"else condition")
                out.append(Sum//divide)
                #print("SUm:",Sum,"divide",divide,"res:",Sum//divide)
                Sum -= nums[i-k]
                if (i+k+1)<length:
                    Sum += nums[i+k+1]
        return out