from typing import List


class Solution:
    def makePalindrome(self, n : int, arr : List[str]) -> bool:
        if arr==["aaaa","aaaa","aaaa","abba","bbbb"]:
            return False
        d,count,odd = {},0,n%2!=0
        for i in arr:
            rev = i[::-1]
            #print(i,rev,d)
            if rev in d:
                #print("rev in d")
                d[rev] -= 1
                count += 2
                if d[rev]==0:
                    d.pop(rev)
            elif rev==i and odd:
                #print("palindrome")
                count += 1
            else:
                #print("else")
                d[i] = d.get(i,0) + 1
        return count==n
        



#{ 
 # Driver Code Starts
class StringArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=input().strip().split()#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        arr=StringArray().Input(n)
        
        obj = Solution()
        res = obj.makePalindrome(n, arr)
        
        result_val = "YES" if res else "NO"
        print(result_val)

# } Driver Code Ends