class Solution:
    def countPairs(self, nums: List[int]) -> int:
        n,ans = len(nums),0
        for i in range(n):
            for j in range(i+1,n):
                num1,num2,count,set1,set2 = nums[i],nums[j],0,set(),set()
                while num1>0 or num2>0:

                    if num1%10!=num2%10 : 
                        count += 1
                        set1.add(num1%10)
                        set2.add(num2%10)
                    num1 //= 10
                    num2 //= 10
                if nums[i]==nums[j]: ans += 1
                elif count<=2 and len(set1.intersection(set2))>=count: ans += 1
                #print(nums[i],nums[j],count,set1.intersection(set2),ans)
        return ans