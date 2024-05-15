class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k%len(nums)
        new = deque(nums)
        new.rotate(k)
        nums.clear()
        nums.extend(new)
        return nums
