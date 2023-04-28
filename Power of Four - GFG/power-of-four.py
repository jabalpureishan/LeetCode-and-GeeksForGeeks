# you may use python module's
# just return true/false or 1/0
class Solution():
    def isPowerofFour(self, n):
        n = str(bin(n))
        #print(n)
        if n[2]!="1":
            return False
        n = n[3:]
        #print(n)
        z = n.count("0")
        o = n.count("1")
        #print("z:",z,"o",o)
        if z%2==0 :
            if o==0:
                return True
        return False


#{ 
 # Driver Code Starts
# Your code goes here

if __name__=='__main__':
    test = int(input())
    for i in range(test):
        num = int(input())
        if(Solution().isPowerofFour(num)):
            print (1)
        else:
            print (0)
# } Driver Code Ends