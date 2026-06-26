class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # we can down ,diagonally left or right so three recursion conditions 
        # the initial step will be from 0,0 anc 
        # the end case will be the last row at 
        def traverse(i,j,m,n,dp):
            
            # and the out of bound conditions as we r going down and along the diagonals 
            if(j<0 or j>=n):
                return float("inf")
            # base case when it reaches end i.e i==0 then return the value
            if(i==m-1):
                return matrix[i][j]
            
            # dp condition
            if dp[i][j] is not None:
                return dp[i][j]

            # now comes the recursion case 
            down=matrix[i][j]+traverse(i+1,j,m,n,dp)
            left_diag=matrix[i][j]+traverse(i+1,j-1,m,n,dp)
            right_diag=matrix[i][j]+traverse(i+1,j+1,m,n,dp)

            # now find the minimum of all of these and return it ?
            dp[i][j]=min(down,left_diag,right_diag)

            return dp[i][j]


        # pass the initial points to the function
        m=len(matrix)
        n=len(matrix[0])

        # comment the below dp lines to recursion solution
        dp=[[None for _ in range(n)] for _ in range(n)]

        ans = float("inf")
        for j in range(n):
            ans = min(ans, traverse(0, j, m, n,dp))

        return ans