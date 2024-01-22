class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        sum_,ans,d = 0,[],{}
        n = len(nums)
        for i in range(n):
            curr = nums[i]
            sum_ += curr
            d[curr] = d.get(curr,0) + 1
            if d[curr]>1:
                ans.append(curr)
                break
        sum_ += sum(nums[i+1:])
        #print("sum:",sum_)
        sum_ -= ans[0]
        #print(sum_)
        ans.append((n*(n+1))//2-sum_)
        return ans
        