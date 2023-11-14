class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        from math import sqrt
        def divisors(n):
            ans = n+1
            count = 2
            i = 2
            while i<=sqrt(n):
                if n%i==0:
                    ans += i
                    count += 1
                    if i!=n//i:
                        ans += n//i  
                        count += 1                                             
                i += 1
            if count==4:
                return ans
            return 0
        sum_ = 0
        for i in nums:
            sum_ += divisors(i)
        return sum_ 
        