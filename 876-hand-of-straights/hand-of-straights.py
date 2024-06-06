from collections import Counter
from sortedcontainers import SortedDict
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n%groupSize!=0:
            return False
        hand = SortedDict(Counter(hand))
        for i in range(n//groupSize):
            for j in hand:
                break
            #print("j:",j)
            hand[j] -= 1
            if hand[j]==0:
                hand.pop(j)
            for m in range(j+1,j+groupSize):
                #print("m",m)
                if m in hand:
                    hand[m] -= 1
                    if hand[m]==0:
                        hand.pop(m)
                else:
                    return False
            #print(hand)
        return True