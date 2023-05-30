class Solution:
    def maximum(s,chars,vals):
        d = {}
        length = len(chars)
        for i in range(length):
            d[chars[i]] = vals[i]
        Max = float("-inf")
        curr = 0
        for i in s:
            if i in d:
                curr += d[i]
            else:
                curr += ord(i) - 96
            if curr>Max :
                Max = curr
            if curr<0 :
                curr = 0
        Max = max(0,Max)
        return Max

    print(maximum("abc","abc",[-1,-1,-1]))
    print(maximum("adaa","d",[-1000]))
