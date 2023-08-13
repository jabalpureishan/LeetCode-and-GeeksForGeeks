#User function Template for python3


class Solution:
    def SortedString(self, s:str) -> str:
        v  = {"a","e","i","o","u"}
        first = s[0] in v
        #  ! first true matlab pehla vowel
        s = sorted(s)
        vowels,consonant,ans = [],[],""
        for i in s:
            if i in v:
                vowels.append(i)
            else:
                consonant.append(i)
        lenc,lenv = len(consonant),len(vowels)
        Min = min(lenc,lenv)
        for i in range(Min):
            if first:
                ans += vowels[i]
                ans += consonant[i]
            else:
                ans += consonant[i]
                ans += vowels[i]
        if lenc>Min:
            ans += "".join(consonant[Min:])
        else:
            ans += "".join(vowels[Min:])
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		s=input()
		ob = Solution()
		ans = ob.SortedString(s)
		print(ans)
# } Driver Code Ends