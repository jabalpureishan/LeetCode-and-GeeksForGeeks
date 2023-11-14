#User function Template for python3

class Solution:
    def sieveOfEratosthenes(self, N):
        def isprime(n):
            if n==2 or n==3:
                return True
            if n==1 or n%2==0 or n%3==0:
                return False
    
            i= 5
            while i*i<=n:
                if n%i==0 or n%(i+2)==0:
                    return False
                i += 6
            return True

        return list(filter(lambda x:isprime(x),range(1,N+1))) 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sieveOfEratosthenes(N)
        for i in ans:
            print(i, end=" ")
        print()
# } Driver Code Ends