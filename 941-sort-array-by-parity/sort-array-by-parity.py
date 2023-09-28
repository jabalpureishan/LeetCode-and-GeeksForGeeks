class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        Output = []
        for i in nums:
            if i%2==0 :
                even.append(i)
            else:
                odd.append(i)
        Output.extend(even)
        Output.extend(odd)
        return Output
        