class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = []
        curr = chars[0]
        chars.append("~")
        count = 0
        for i in range(len(chars)):
            if chars[i]==curr:
                count += 1
            else:
                ans.append(curr)
                if count!=1:
                    for j in str(count):
                        ans.append(j)
                curr = chars[i]
                count = 1
        chars.clear()
        chars.extend(ans)
        return len(chars)