class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary = set(dictionary)
        sentence = sentence.split(" ")
        for ind,i in enumerate(sentence):
            for j in range(1,len(i)+1):
                curr = i[:j]
                if curr in dictionary:
                    sentence[ind] = curr
                    break
        return " ".join(sentence) 

        