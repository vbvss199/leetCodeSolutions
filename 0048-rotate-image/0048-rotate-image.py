class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # # create a deep copy instead of shallow ones 
        # copy = [row[:] for row in matrix]
        # # as rows and columns are same so n is same
        # n=len(matrix[0])
        # for i in range(n):
        #     for j in range(n):
        #         matrix[j][n-1-i]=copy[i][j]
        # return matrix

        # lets solve this in O(1) space complexity 
        n=len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            row.reverse()
        return matrix