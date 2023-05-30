from collections import defaultdict

class Solution:
    def score(nums):
        length = len(nums)
        score = 0 
        mark = set()
        counts = defaultdict(int)
        
        for num in nums:
            counts[num] += 1
        
        min_val = min(nums)
        
        while len(mark) < length:
            score += min_val
            
            # Reduce the count of the current minimum value
            counts[min_val] -= 1
            if counts[min_val] == 0:
                del counts[min_val]
            
            # Update the minimum value from the remaining values
            min_val = min(counts.keys())
            
            # Find the next unmarked index with the minimum value
            min_index = nums.index(min_val)
            while min_index in mark:
                min_index = nums.index(min_val, min_index + 1)
            
            mark.add(min_index)
            print("*")
        
        return score

print(Solution.score([2,3,5,1,3,2]))
print(Solution.score([2,1,3,4,5,2]))
