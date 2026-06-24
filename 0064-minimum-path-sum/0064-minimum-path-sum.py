class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # find the path from the top to bottom and store the one which has minimum!!!!
        # the unique paths is the one which has number of paths but here we need to return the sum which is minimum 
        # explore all the paths while travswrsing track the sum and compare and stor ethe minimum sum there it sekf wnd return it 

        # as it can traverse left or right recursively 
        def traverse(i,j,m,n,dp):
            if i==m-1 and j==n-1:
                return grid[i][j]

            if i>=m or j>=n:
                # this one is out of the bound condition 
                # return the max_path which we cannot consider 
                max_int=float("inf")
                return max_int
            
            # dp condition 
            if dp[i][j]!=-1:
                return dp[i][j]

            # and here comes the recursive condition 
            down=grid[i][j]+traverse(i,j+1,m,n,dp)
            right=grid[i][j]+traverse(i+1,j,m,n,dp)

            dp[i][j]= min(down,right)

            return dp[i][j]


        # pass the initial points to the traverse 
        # where 0,0 is the initial starting point 
        # rows
        m=len(grid)
        n=len(grid[0])
        dp=[[-1 for _ in range(n)] for _ in range(m)]
        return traverse(0,0,m,n,dp)

        # overlapping sub problems ?
        # replace the last return with dp[i][j] where i is m-1 and j is n-1 
        # if there is state previously why dont we return it instead of calling again so 
