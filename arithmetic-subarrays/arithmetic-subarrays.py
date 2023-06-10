class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def check(arr):
            arr.sort(reverse=True)
            D = arr[0] - arr[1]
            for i in range(len(arr)-1):
                if arr[i] - arr[i+1] != D :
                    return False
            return True
        output = []
        for i in range(len(l)):
            output.append(check(nums[l[i]:r[i]+1]))
        return output