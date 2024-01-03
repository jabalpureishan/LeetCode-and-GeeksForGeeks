class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = ans = 0
        for i in bank:
            curr = i.count("1")
            if curr>0:
                if prev==0:
                    prev = curr
                else:
                    ans += prev*curr
                    prev = curr
        return ans
        