from sortedcontainers import SortedList
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        length = len(nums)
        List = SortedList(nums[:k])
        output = []
        if List[x-1]<0:
            output.append(List[x-1])
        else:
            output.append(0)
        slides = length - k
        window = k
        for j in range(slides):
            List.remove(nums[j])
            List.add(nums[window])
            window += 1
            if List[x-1]<0:
                output.append(List[x-1])
            else:
                output.append(0)
        return output