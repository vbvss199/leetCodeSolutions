class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # use O(m+n) to get the best case 
        # lets create separate arrays for tracking the zeros at the respective indices
        # list size auto updates dynamically 
        # to get the matrix rows and columns
        m=len(matrix)
        n=len(matrix[0])
        row=[0]*m
        col=[0]*n
        for i in range(0,m):
            for j in range(0,n):
                if(matrix[i][j]==0):
                    row[i]=1
                    col[j]=1
        for i in range(0,m):
            for j in range(0,n):
                if(row[i] or col[j]):
                    matrix[i][j]=0
        return matrix