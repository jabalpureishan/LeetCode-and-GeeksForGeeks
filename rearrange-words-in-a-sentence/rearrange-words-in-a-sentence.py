class Solution:
    def arrangeWords(self, text: str) -> str:
        text = text.split(" ")
        for i in range(len(text)):
            text[i]= text[i].lower()
            

        text.sort(key = lambda x:len(x))
        text[0] = text[0].capitalize()
        text = " ".join(text)
        return text