from sortedcontainers import SortedList
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        output = []
        List = SortedList(nums[:k])
        window = k
        slides = len(nums) - k
        if k%2!=0 :
            output.append(float(List[(k-1)//2]))
            for i in range(slides):
                List.remove(nums[i])
                List.add(nums[window])
                window += 1
                output.append(float(List[(k-1)//2]))
        else:
            mid = k//2
            output.append((List[mid]+List[mid-1])/2)
            for i in range(slides):
                List.remove(nums[i])
                List.add(nums[window])
                window += 1
                output.append((List[mid]+List[mid-1])/2)
        return output

