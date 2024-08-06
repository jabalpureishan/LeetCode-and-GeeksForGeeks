class Solution:
    def minimumPushes(self, word: str) -> int:
        word = Counter(word)
        word = sorted(word.items(),key=lambda x:x[1],reverse=True)
        num,cost,mult = 1,0,1
        for i in word:
            curr = mult*i[1]
            cost += mult*i[1]
            if num%8==0:
                mult += 1
            num += 1
        return cost
        