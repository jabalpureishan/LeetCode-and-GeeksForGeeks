class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        bob = sum(possible)
        n = len(possible)
        bob += -(n-bob)
        dan = 0
        for ind in range(n-1):
            if possible[ind]==0:
                bob += 1
                dan -= 1

            else:
                bob -= 1
                dan += 1
            #print(dan,bob)
            if dan>bob:
                return ind+1
        return -1