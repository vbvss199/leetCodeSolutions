class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        copy = [row[:] for row in matrix]
        # as rows and columns are same so n is same
        n=len(matrix[0])
        for i in range(n):
            for j in range(n):
                matrix[j][n-1-i]=copy[i][j]
        return matrix