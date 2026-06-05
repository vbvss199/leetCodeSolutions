class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # the only path it can go is i+1 j+1 whic is down iterate through the loop and check if it is equal to m and nt thn count the possibilities 
        
        # traverse through this path via dfs then we can count it 
        # def traverse(i,j):
        #     if((i==m-1) and (j==n-1)):
        #         return 1
        #     if (i>=m or j>=n):
        #         return 0 
        #     # traverse right and down 
        #     down = traverse(i + 1, j)
        #     right = traverse(i, j + 1)

        #     return down+right 
        # return traverse(0,0)


        # def paths(i,j):
        #     # base case will be if i ==0 and j==0 then return 1
        #     if(i==0 and j==0):
        #         return 1
        #     if(i<0 or j<0 or j==m or j==n):
        #         return 0
        #     else:
        #         return paths(i,j-1) + paths(i-1,j)

        # this will fail due to TC , lets go through the Dp (recursion and using array) and tc is O(2*(m*n)) which is 2 decisions for the any position and m*n is the size of the grid  and space is O(m*n) the above is recursion 

        # lets use memoisation
        memo={}
        def paths(i,j):
            if i==m-1 and j==n-1:
                return 1
            if i>=m or j>=n:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            memo[(i,j)]=paths(i+1,j)+paths(i,j+1)
            return memo[(i,j)]
        return paths(0,0)