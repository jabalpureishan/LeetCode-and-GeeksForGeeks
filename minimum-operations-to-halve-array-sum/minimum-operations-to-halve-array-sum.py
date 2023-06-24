import heapq
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        half = sum(nums)/2
        heap = []
        heapq.heapify(heap)
        for i in nums:
            heappush(heap,-1*i)
        count,current = 0,0
        while(current<half):
            current += (-1*heap[0])/2
            count += 1
            heappush(heap,heap[0]/2)
            heappop(heap)
        return count   