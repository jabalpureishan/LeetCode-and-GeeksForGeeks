class Solution:
    def flip(a,n):
        for i in range(n):
            if a[i]==0:
                a[i] = 2
        Max_Sum,ones= a[0],0
        curr = a[0]
        for i in range(1,n):
            if (curr + a[i])>a[i] :
                curr += a[i]
            else:
                curr = a[i]
            if curr>Max_Sum :
                Max_Sum = curr
                

        return Max_Sum
            



    print(flip([1,0,0,1,0],5))
    print(flip([1,0,0,1,0,0,1],7))
    print(flip([1,1,1,1,0,0,1,0],8))
    print(flip([1,1,1,0,0,1,1,1,0,0],9))