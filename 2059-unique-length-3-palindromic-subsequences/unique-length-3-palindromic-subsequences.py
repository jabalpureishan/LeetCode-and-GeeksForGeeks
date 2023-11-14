class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n,count,d = len(s),0,{}
        for i in range(n):
            if s[i] in d:
                d[s[i]].append(i)
            else:
                d[s[i]] = [i]
        #print(d)
        for i in d:
            count += len(set(s[d[i][0]+1:d[i][-1]]))
        return count