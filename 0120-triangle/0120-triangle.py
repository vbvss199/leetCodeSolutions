class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # to return the minimum path sum from top to bottom , you may move to the adjacent rows below!
        # so we may move to the next row j or j+1

        def traverse(i,j,m,dp):
            # the base case is fucked up write down the correct one  when we reach the last row then return the element 
            # if(i==m-1) and (j==n-1):
            #     return triangle[i][j]
            if(i==m-1):
                return triangle[i][j]
            
            if dp[i][j] is not None:
                return dp[i][j]

            # now comes the here recursion 
            adj1=traverse(i+1,j,m,dp)
            adj2=traverse(i+1,j+1,m,dp)

            # now return the minimum of the both 
            dp[i][j]=triangle[i][j]+min(adj1,adj2)

            return dp[i][j]
        

        # call the traverse with the initial values 
        # rows and columns 
        m=len(triangle)
        # dp = [[-1 for _ in range(m)] for _ in range(len(triangle))]
        dp = [[None for _ in row] for row in triangle]
        # return the function value
        return traverse(0,0,m,dp)


        # if want tonintroduce dp just create a 2d array dp[i][j] where i and j are length of the m and n 
        # dp[i][j]=[[-1 for _ in range(n)] for _ in range(m)] but here shape is not same 


        # lets talk about the time complexity for each row the columns are 1,2,3,4,...n+1 and for each element in the row there are like 2,2^2,2^3 which is exponential 
        # and for the recursion space complexity is  O(n) 


        # are there overlapping sub problems ?
        # draw the recursion tree and if there are any sub problems then answer is yes 
        # then decide the number of rows and columns which are n rows and n columns 
        # after memoisation the TC is O(m*n) ot O(n*n) 
        # for triangle 1+2+3+4+... states which is n*n+1/2 which is O(n*2)
        # Brute force recursion	2ⁿ paths
        # DP (memoized)	~ number of unique nodes


        # recursion is always a top down 




        # lets decrease the TC using the tabulation which is the opposute o the recursion top down 
        # recursion 0 to n-1
        # tabulation n-1 to 0 
        # dp[n][n] so write the basde case as dp[n-1][j] and run j from 0 to n-1 
        # for j in range(0,n):
        # dp[n-1][j]=triangle[n-1][j]

        # as already n-1 is done now go to n-2 