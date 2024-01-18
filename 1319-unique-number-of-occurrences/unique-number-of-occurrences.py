class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr = Counter(arr)
        arr = list(arr.values())
        return len(arr)==len(set(arr)) 
        