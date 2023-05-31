class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {"a","e","i","o","u"}
        out = ""
        for i in words:
            if((i[0] in vowels) and (i[-1] in vowels)):
                out += "1"
            else:
                out += "0"
        output = []
        for i in queries:
            output.append(out.count("1",i[0],i[1]+1))
        return output