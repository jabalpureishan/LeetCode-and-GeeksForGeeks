class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n,c,count = len(word),0,0
        for i in range(n):
            d,c = {"a":0,"e":0,"i":0,"o":0,"u":0},0
            for j in range(i,n):
                if word[j] in d: d[word[j]] += 1
                else: c +=1
                if min(d.values())>0 and c==k: count += 1
        return count