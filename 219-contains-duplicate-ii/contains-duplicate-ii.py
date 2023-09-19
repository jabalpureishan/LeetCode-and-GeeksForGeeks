class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        k += 1
        window = set(nums[:k])
        if sorted(window)!=sorted(nums[:k]):
            return True
        slides = len(nums)-k
        for i in range(slides):
            window.remove(nums[i])

            if nums[k] in window:
                return True
            window.add(nums[k])
            k += 1
            #print(window)
        return False