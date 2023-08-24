class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        def splitted(a, b):
            result = ([a//b + 1] * (a%b) + [a//b] * (b - a%b))
            return(result)

        #words = deque(words)
        ans,word,length,last = [],0,0,0
        for i in range(len(words)-1):
            word += 1
            length += len(words[i])
            if (length + len(words[i+1]) + word)>maxWidth:
                res = ""
                if word==1:
                    res += words[last]
                    res += " "*(maxWidth-len(words[last]))
                else:
                    spaces = splitted(maxWidth-length,word-1)
                    #print("spaces:",spaces,"last:",last,"last+word-1:",last+word-1)
                    ind = 0
                    for j in range(last,last+word-1):
                        res += words[j]
                        res += " "*spaces[ind]
                        ind += 1
                    res += words[last+word-1]
                #print("len:",len(res))
                word = length = 0
                last = i+1
                ans.append(res)
                #print("ans:",ans,"last:",last)
        #print("last:",last,"length:",len(words))
        length = word = 0
        res = ""
        for i in range(last,len(words)):
            length += len(words[i])
            word += 1
            res += words[i]
            if len(res)<maxWidth:
                res += " "
        res += " "*(maxWidth-len(res))
        ans.append(res)
        return ans