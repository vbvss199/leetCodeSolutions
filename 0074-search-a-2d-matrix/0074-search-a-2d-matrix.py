class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        columns=len(matrix[0])
        low,high=0,rows*columns-1
        while(low<=high):
            mid=(low+high)//2
            row_idx=mid//columns
            col_idx=mid%columns
            midElement=matrix[row_idx][col_idx]
            if(target==midElement):
                return True
            elif(midElement<target):
                low=mid+1
            else:
                high=mid-1
        return False

        
        