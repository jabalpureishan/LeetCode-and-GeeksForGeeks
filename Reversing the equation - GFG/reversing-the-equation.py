#User function Template for python3

class Solution:
    def reverseEqn(self, s):
        numbers = []
        other = []
        current = ""
        s += "$"
        for i in s:
            if i.isdigit():
                current += i
            else:
                numbers.append(current)
                other.append(i)
                current = ""
        output = "" 
        other.pop()
        for i in range(-1,-(len(numbers)),-1):
            output += numbers[i] + other[i]
        output += numbers[0]
        return output


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.reverseEqn(s)
        print(ans)
# } Driver Code Ends