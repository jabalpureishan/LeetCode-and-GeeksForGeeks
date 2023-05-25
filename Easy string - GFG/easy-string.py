#User function Template for python3

class Solution:

    def transform(self, S):
        S = S.lower()
        output = ""
        current = S[0]
        S += "$"
        count = 0
        for i in S:
            if i==current:
                count += 1
            else:
                output += str(count) + current
                count = 1
                current = i
        return  output


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        solObj = Solution()

        print(solObj.transform(S))
# } Driver Code Ends