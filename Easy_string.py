class Solution:
    def  transform(S):
        S = S.lower()
        output = ""
        current = S[0]
        S += "$"
        count = 0
        for i in S:
            if i==current:
                count += 1
            else:
                output += str(count) + current
                count = 1
                current = i
        return  output

    print(transform("aaABBb"))
    print(transform("aaacca"))