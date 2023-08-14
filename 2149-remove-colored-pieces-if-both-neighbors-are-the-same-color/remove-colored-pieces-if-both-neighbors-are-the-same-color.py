class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice,bob = 0,0
        for i in range(1,len(colors)):
            if colors[i-1:i+2]=="AAA":
                alice += 1
            elif colors[i-1:i+2]=="BBB":
                bob += 1
        return alice>bob