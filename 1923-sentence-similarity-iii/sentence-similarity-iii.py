class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # s1 = sentence1.split(" ")
        # s2 = sentence2.split(" ")
        # #print(s1,s2)
        # s,b = min(s1,s2,key = lambda x:len(x)),max(s2,s1,key = lambda x:len(x))
        # print(s,b)
        # if len(s)==1 and s[0]==b[0] or s[0]==b[-1]:
        #     return True
        # if s[0]==b[0] and s[-1]==b[-1]:
        #     return True
        # return False
        s1 = sentence1.split(" ")
        s2 = sentence2.split(" ")
        #print(s1,s2)
        s,b = min(s1,s2,key = lambda x:len(x)),max(s2,s1,key = lambda x:len(x))
        ind = count = 0
        while ind<len(s) and s[ind]==b[ind]:
            ind += 1
            count += 1
        ind -= 1 
        ind -= len(s)
        index = -1
        #print(ind,index)
        while index>ind and s[index]==b[index]:
            index -= 1
            count += 1
        #print(count)
        return count==len(s)
        