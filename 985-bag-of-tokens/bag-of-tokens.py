class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        n,start,score = len(tokens),0,0
        end = n-1
        tokens.sort()
        Max = 0
        while start<n and tokens[start]<=power and start<=end:
            power -= tokens[start]
            score += 1
            Max = max(Max,score)
            start += 1
            #print("b start:",start,"end:",end,"power:",power,"score:",score)
            if start<n and tokens[start]>power:
                power += tokens[end]
                score -= 1
                end -= 1
            
            #print("after start:",start,"end:",end,"power:",power,"score:",score)
        return Max
            