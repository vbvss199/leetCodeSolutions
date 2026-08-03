class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # given n we have to return all the possible combinations 
        combinations=[]
        # recursion yeah but we need to consider both the parenthesis 
        # consider i and j 
        def dfs(current,i,j,n,combinations):
            if(len(current)==2*n):
                combinations.append(current)
            if i<n:
                dfs(current+"(",i+1,j,n,combinations)
            if j<i:
                dfs(current+")",i,j+1,n,combinations)
            return combinations

        # pass the number of the params we need to consider , where n for the left and n for the right 
        return dfs("",0,0,n,combinations)
        