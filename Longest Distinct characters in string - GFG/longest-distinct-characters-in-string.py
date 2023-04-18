#User function Template for python3

class Solution:

    def longestSubstrDistinctChars(self, S):
        if not S:
            return 0
        
        char_dict = {}
        start = 0
        max_length = 0
        
        for i, char in enumerate(S):
            if char in char_dict and char_dict[char] >= start:
                start = char_dict[char] + 1
            else:
                max_length = max(max_length, i - start + 1)
            char_dict[char] = i
        
        return max_length


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        solObj = Solution()

        ans = solObj.longestSubstrDistinctChars(S)

        print(ans)

# } Driver Code Ends