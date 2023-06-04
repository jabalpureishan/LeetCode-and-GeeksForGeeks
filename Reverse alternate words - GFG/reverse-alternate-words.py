#User function Template for python3

class Solution:

    def reverseAlternate(self, Str):
        Str = Str.split(" ")
        for i in range(1,len(Str),2):
            Str[i] = Str[i][::-1]
        Str = " ".join(Str)
        return Str


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):

        Str = input()

        solObj = Solution()

        print(solObj.reverseAlternate(Str))

# } Driver Code Ends