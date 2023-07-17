#User function Template for python3

class Solution:
    def longestUniqueSubsttr(self, S):
        s=S
        left = 0
        length = len(s)
        set_ = set()
        Max = 0
        for right in range(length):
            if s[right] in set_:
                while(left<right):
                    set_.discard(s[left])
                    left += 1
                    if s[left-1]==s[right]:
                        break
            set_.add(s[right])
            Max = max(Max,len(set_))
        return Max


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        s = input().strip()
        
        
        ob=Solution()
        print(ob.longestUniqueSubsttr(s))
# } Driver Code Ends