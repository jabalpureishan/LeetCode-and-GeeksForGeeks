class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        oddn = ceil(n/2)
        evenn = n-oddn
        oddm = ceil(m/2)
        evenm = m-oddm
        return evenm*oddn + evenn*oddm
        