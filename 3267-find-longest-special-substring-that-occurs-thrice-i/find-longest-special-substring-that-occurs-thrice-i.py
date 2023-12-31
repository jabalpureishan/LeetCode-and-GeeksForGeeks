class Solution:
    def maximumLength(self, s: str) -> int:
        d,n = {},len(s)
        for i in range(n-2,0,-1):
            slides = n-i+1
            window = i
            # curr = Counter(s[:i])
            # if len(curr)==1:
            #     d[s[:i]] = d.get(s[:i],0) + 1
            for j in range(slides):
                curr = s[j:window]
                if len(set(curr))==1:
                    d[curr] = d.get(curr,0) + 1
                    if d[curr]>=3:
                        return window-j
                # curr[s[window]] = curr.get(s[window],0) + 1
                # curr[s[j]] -= 1
                # if curr[s[j]]==0:
                #     curr.pop(s[j])
                # if len(curr)==1:
                #     d[s[j:window]] = d.get(s[j:window],0) + 1
                #     if d[s[j:window]]>=3:
                #         #print(curr)
                #         return window-j
                window += 1
        return -1
        