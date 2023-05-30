def driver():  
    Test = int(input(""))
    for i in range(Test):  
        N,K = input().split()
        N,K = int(N),int(K)
        count = 0
        while(N!=0):
            if(N%K==0):
                N = N//K
                count = count + 1
            else:
                P=N%K
                count = count + P
                N = N - P
        print(count)


driver()

            

