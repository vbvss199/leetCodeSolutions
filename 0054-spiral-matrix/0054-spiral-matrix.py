class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m=len(matrix)
        n=len(matrix[0])
        top=0
        left=0
        right=n-1
        bottom=m-1
        mat=[]
        while top <= bottom and left <= right:
            # first case from left to right
            for i in range(left,right+1):
                mat.append(matrix[top][i])
            top+=1
            # second case from top to bottom
            for i in range(top,bottom+1):
                mat.append(matrix[i][right])
            right-=1
            # third goes from right to left
            if(top<=bottom):
                for i in range(right,left-1,-1):
                    mat.append(matrix[bottom][i])
                bottom-=1
            # fourth goes from bottom to top
            if(left<=right):
                for i in range(bottom,top-1,-1):
                    mat.append(matrix[i][left])
                left+=1
        return mat

         