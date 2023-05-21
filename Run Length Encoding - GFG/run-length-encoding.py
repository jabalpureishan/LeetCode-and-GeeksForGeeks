from collections import OrderedDict
def encode(arr):
    arr = arr + "$"
    out = ""
    current = arr[0]
    count = 0
    for i in range(len(arr)):
        if arr[i]==current:
            count += 1
        else:
            out += current + str(count)
            current = arr[i]
            count = 1
    return out
        


#{ 
 # Driver Code Starts
#Your code will prepended here
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        arr=input().strip()
        print (encode(arr))
# } Driver Code Ends