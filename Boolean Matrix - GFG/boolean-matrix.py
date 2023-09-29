#User function Template for python3


#Function to modify the matrix such that if a matrix cell matrix[i][j]
#is 1 then all the cells in its ith row and jth column will become 1.
def booleanMatrix(matrix):
    r,c = set(),set()
    rows = len(matrix)
    columns = len(matrix[0])
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j]==1:
                r.add(i)
                c.add(j)
            
    for i in range(rows):
        for j in range(columns):
            if i in r or j in c:
                matrix[i][j] = 1
    return matrix


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        matrix = []
        for i in range(r):
            line = [int(x) for x in input().strip().split()]
            matrix.append(line)
        booleanMatrix(matrix)
        for i in range(r):
            for j in range(c):
                print(matrix[i][j], end=' ')
            print()


# } Driver Code Ends