class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        k += 1
        window = set()
        for i in range(min(k,len(nums))):
            if nums[i] in window:
                return True
            window.add(nums[i])
        slides = len(nums)-k
        for i in range(slides):
            window.remove(nums[i])

            if nums[k] in window:
                return True
            window.add(nums[k])
            k += 1
            #print(window)
        return False