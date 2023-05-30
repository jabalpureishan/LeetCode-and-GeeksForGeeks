class Solution:
    def count(s):
        s = s.split(" ")
        count = 1
        for i in s:
            dis = len(set(i))
            #print("dis:",dis)
            #print("v:",(dis*(dis+1))//2)
            count *= (dis*(dis+1))//2
        return count%(10**9 + 7)

    print(count("too hot"))
    print(count("aa"))

