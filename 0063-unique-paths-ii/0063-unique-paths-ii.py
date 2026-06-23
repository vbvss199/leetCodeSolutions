class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # the robot can go either down or right at any point 
        # obstacle marked as 1 and a space marked as 0 
        # our task is to find the path with the obstacles 

        # lets code directly using the memoisation 
        memo={}

        # first write the base cases 
        def paths(i,j,m,n):
            # write the recursion logic here 
            if (i==m-1) and (j==n-1) and obstacleGrid[i][j]!=1:
                return 1


             # and out of bound condition where i or j >m-1 or n-1 
            if i>=m or j>=n:
                return 0


            # at any moment if mat[i][j]==1 then return 0 immediately 
            if(obstacleGrid[i][j]==1):
                return 0
            
            if (i,j) in memo:
                return memo[(i,j)]
            memo[(i,j)]=paths(i+1,j,m,n)+paths(i,j+1,m,n)
            return memo[i,j]
            
        

        # find the rows and columns 
        # rows
        m=len(obstacleGrid)
        # columns
        n=len(obstacleGrid[0])
        # give the starting points of the matrix as well as the lengths of the rows and columns 
        return paths(0,0,m,n)