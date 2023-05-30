class Solution:
    def merge(word1,word2):
        l1 = len(word1)
        l2 = len(word2)
        loop = min(l1,l2)
        output = ""
        for i in range(loop):
            output += word1[i] + word2[i]
        if loop==l1:
            output += word2[loop:]
        else:
            output += word1[loop:]
        return output

    print(merge("abc","pqr"))
    print(merge("ab","pqrs"))
    print(merge("abcd","pq"))