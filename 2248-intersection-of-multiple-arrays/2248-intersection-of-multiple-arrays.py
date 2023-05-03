class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        first = set(nums[0])
        for i in range(1,len(nums)):
            #print("i:",set(nums[i]))
            first = first.intersection(set(nums[i]))
            #print(first)
        first = sorted(first)
        return first