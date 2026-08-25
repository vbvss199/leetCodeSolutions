class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        top,left=0,0
        bottom,right=n-1,n-1

        # so we should fill the elements for the matrix in such a way that it should be filling from 1 to n*n including n square 

        # matrix to be returned 
        mat = [[0] * n for _ in range(n)]

        # we strat filling with this variable
        num=1

        while top<=bottom and left <= right:
            # first start filling from the left 
            for i in range(left,right+1):
                mat[top][i]=num
                num+=1
            top+=1

            # second case top will move a little down and it will start from the next one till bottom
            for i in range(top,bottom+1):
                mat[i][right]=num
                num+=1
            right=right-1

            # now we move towards left 

            for i in range(right,left-1,-1):
                mat[bottom][i] = num
                num += 1
            bottom-=1

            # and finally we move from bottom to top
            for i in range(bottom,top-1,-1):
                mat[i][left]=num
                num+=1
            left += 1
        return mat
