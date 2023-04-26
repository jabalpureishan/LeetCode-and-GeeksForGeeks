from collections import OrderedDict
def encode(arr):
    arr = arr + "$"
    out = ""
    first = arr[0]
    count = 0
    for i in range(len(arr)):
        current = arr[i]
        #print("current:",current)
        
        #print("arr[i]",arr[i])
        if arr[i]==first:
            #print("same and count++")
            count += 1
        else:
            #print("not same")
            out += first + str(count)
            #print("out:",out)
            first = current
            count = 1
            #print("first changed to:",first)
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