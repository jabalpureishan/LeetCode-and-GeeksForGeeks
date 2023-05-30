class Solution:
    def count(S):
        count = 0
        for i in S:
            if i.isalpha():
                count += 1
        return count
    print(count("adjfjh23"))
    print(count("n0ji#k$"))