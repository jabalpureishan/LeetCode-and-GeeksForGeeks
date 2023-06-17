from sortedcontainers import SortedList
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        List = SortedList(nums[:k])
        slides  = len(nums) - k
        window = k
        output = []
        output.append(List[-1])
        for i in range(slides):
            List.remove(nums[i])
            List.add(nums[window])
            window += 1
            output.append(List[-1])
        return  output
