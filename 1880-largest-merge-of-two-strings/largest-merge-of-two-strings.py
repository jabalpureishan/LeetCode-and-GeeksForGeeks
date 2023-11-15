class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        p1 = p2 = 0
        l1,l2,ans = len(word1),len(word2),""
        while p1<l1 and p2<l2:
            #print("compare:",word1[p1],word2[p2],p1,p2)
            if word1[p1]>word2[p2]:
                ans += word1[p1]
                p1 += 1
            elif word1[p1]<word2[p2]:
                ans += word2[p2]
                p2 += 1
            else:
                # if l1-p1>l2-p2:
                #     ans += word1[p1]
                #     p1 += 1
                # elif l1-p1<l2-p2:
                #     ans += word2[p2]
                #     p2 += 1
                # else:
                    if word1[p1+1:]>word2[p2+1:]:
                        ans += word1[p1]
                        p1 += 1
                    else:
                        ans += word2[p2]
                        p2 += 1
            #print("res:",p1,p2)
        if p1<l1:
            ans += word1[p1:]
        elif p2<l2:
            ans += word2[p2:]
        return ans
            