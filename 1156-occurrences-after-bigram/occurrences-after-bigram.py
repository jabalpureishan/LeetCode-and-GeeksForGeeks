class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text = text.split(" ")
        ans = []
        window = 2
        slides = len(text) - 1
        for j in range(slides):
            if text[j:window]==[first,second]:
                if window<len(text):
                    ans.append(text[window])
            window += 1
        return ans