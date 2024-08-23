from sortedcontainers import SortedList
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if len(nums)==1: return [nums[0]]
        window = SortedList(nums[:k])
        check = []
        total = 0
        ans = []
        for i in range(1,k):
            if nums[i]==nums[i-1]+1:
                total += 1
            check.append(total)
        for i in range(k,len(nums)):
            
            if nums[i]==nums[i-1]+1:
                total += 1
            check.append(total)
            #print(i,check)
            if i-k==0 and check[i-2]==k-1 or check[i-2]-check[i-k-1]==k-1:
                ans.append(window[-1])
            else:
                ans.append(-1)
            window.add(nums[i])
            window.remove(nums[i-k])
        i+=1
        if i-k==0 and check[i-2]==k-1 or check[i-2]-check[i-k-1]==k-1:
            ans.append(window[-1])
        else:
            ans.append(-1)
        return ans