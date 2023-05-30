class Solution:
    def search(board,word):
        length = len(word)
        m = len(board)#rows
        n = len(board[0])#columns
        hogaya = set()
        def search(a,b):
            count = 1
            print("search ko aya",a,b)
            while(count<length):
                print("current: ",board[a][b])
                #upar
                if a-1>=0 and board[a-1][b]==word[count] and ((a-1,b) not in hogaya):
                    count += 1
                    a -= 1
                    print("upar count :",count,"current:",board[a][b])
                    hogaya.add((a,b))
                    pass
                elif a+1<m and board[a+1][b]==word[count] and ((a+1,b) not in hogaya):
                    count += 1
                    a += 1
                    print("niche count :",count,"current:",board[a][b])
                    hogaya.add((a,b))
                    pass
                elif b-1>=0 and board[a][b-1]==word[count] and ((a,b-1) not in hogaya):
                    count += 1
                    b -= 1
                    print("left count :",count,"current:",board[a][b])
                    hogaya.add((a,b))
                    hogaya.add
                    pass
                elif b+1<n and board[a][b+1]==word[count] and ((a,b+1) not in hogaya):
                    count += 1
                    b += 1
                    print("right count :",count,"current:",board[a][b])
                    hogaya.add((a,b))
                    pass
                else:
                    print("nahi mila")
                    break
            else:
                return True
            return False

        found = False
        if found==False:
            for i in range(m):
                if found==False:
                    for j in range(n):
                        if board[i][j]==word[0]:
                            print("pehla milgaya:",board[i][j])
                            hogaya.add((i,j))
                            print("hogaya",hogaya)
                            if search(i,j):
                                
                                found = True
                                break
                            else:
                                hogaya.remove((i,j))
                                print("remove kiya")
                            print("hogaya",hogaya)
                                
        return found

    print(search([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED"))
    print("___________")
    print(search([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCB"))
    print("___________")
    print(search([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"SEE"))
    print("___________")
    print(search([["a","b"]],"ba"))

