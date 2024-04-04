class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        nums.append(float("inf"))
        n = len(nums)
        ans = count = 0

        for i in range(n-1):
            # print("nums[i]",nums[i])
            if nums[i]!=nums[i-1]:
                count += 1
                # print("not eqaul count:",count)
            else:
                ans += (count*(count+1))//2
                # print("equal count:",count,"ans:",ans)
                count = 1
        ans += (count*(count+1))//2
        return ans
        