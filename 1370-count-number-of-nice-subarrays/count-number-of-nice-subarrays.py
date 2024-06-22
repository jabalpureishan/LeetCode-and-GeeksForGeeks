class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        d = {0:1}
        count,odd = 0,0
        for i in nums:
            if i%2!=0:
                odd += 1
            d[odd] = d.get(odd,0) + 1
            count += d.get(odd-k,0)
        return count


        