def countPalinInRange (n, s, q1, q2):
    Min = min(q1,q2)
    Max = max(q1,q2)
    S = s[Min:Max+1]
    count = 0
    length = Max - Min + 1
    for i in range(1,length+1):
        window = i
        slides = length - window + 1
        for j in range(slides):
            res = S[j:window]
            if res==res[::-1]:
                count += 1
            window += 1
    return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    n = int (input ())
    s = input ()
    q1, q2 = list(map(int, input().split()))
    print (countPalinInRange (n, s, q1, q2))
    
# Contributed By: Pranay Bansal

# } Driver Code Ends