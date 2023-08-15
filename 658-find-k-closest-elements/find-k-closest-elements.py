class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr = sorted(arr,key=lambda y : abs(x-y))
        return sorted(arr[:k])