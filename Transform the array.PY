class Solution:
    def transform(arr,n):
        new,zeroes = [],[]
        for i in arr:
            if i==0:
                zeroes.append(0)
            else:
                new.append(i)
        print(new)
        while(True):
            for i in range(1,len(new)):
                if new[i]==new[i-1]:
                    new[i-1] = 2*new[i-1]
                    new.pop(i)
                    zeroes.append(0)
                    break
            else:
                break
        new.extend(zeroes)
        return new


    print(transform([2, 4, 5, 0, 0, 5, 4, 8, 6, 0, 6, 8],12))
    print(transform([1 ,5, 6, 0, 0 ,6 ,0 ,12, 8 ,0 ,8 ,8],12))   



        

