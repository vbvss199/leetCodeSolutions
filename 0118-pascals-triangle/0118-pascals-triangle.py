class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # the approach will be r-1Cn-1 
        # temp.add(n-1Cr-1) then after the loop add the temp to the answer list 
        # answer list is a list of lists 
        ansList=[]
        def calCombination(n, r):
            # computes nCr using integer math
            res = 1
            for i in range(r):
                res = res * (n - i) // (i + 1)
            return res
        for i in range(1,numRows+1):
            temp=[]
            for j in range(i):
                temp.append(calCombination(i-1,j))
            ansList.append(temp)
        return ansList
        