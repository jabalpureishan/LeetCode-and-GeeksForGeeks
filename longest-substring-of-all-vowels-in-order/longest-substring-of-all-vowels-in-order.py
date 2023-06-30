class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        Max = 0
        count = 1
        alpha = {"a","e","i","o","u"}
        length = len(word)
        #if length==1:
            #return 1
        word += "@"
        set_ = {word[0]}
        for i in range(1,length+1):
            #print("word[i]",word[i])
            if((word[i] in alpha) and (ord(word[i])>=ord(word[i-1]))):
                    set_.add(word[i])
                    #print("set:",set_)
                    count += 1
            else:
                #print("set:",set_)
                if len(set_)==5:
                    #print("count:",count)
                    Max = max(Max,count)
                count = 1 
                set_ = {word[i]}

        return Max