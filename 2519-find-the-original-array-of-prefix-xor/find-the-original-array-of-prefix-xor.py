class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        def find(x,z):
            y = z ^ x
            return int(bin(y)[2:], 2)

        length = len(pref)
        curr = pref[0]
        ans = [curr]
        for i in range(1,length):
            temp = find(curr,pref[i])
            curr ^= temp
            ans.append(temp)
        return ans
        