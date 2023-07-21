class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        ind = set()
        bulls = cows = 0
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                bulls += 1
            else:
                ind.add(i)
        d = {}
        for i in ind:
            d[secret[i]] = d.get(secret[i],0) + 1
        #print(ind)
        #print(d)
        for i in ind:
            #print("guess[i]:",guess[i],"d:",d)
            if guess[i] in d:
                cows += 1
                d[guess[i]] -= 1
                if d[guess[i]]==0:
                    d.pop(guess[i])
        return str(bulls)+"A"+str(cows)+"B"