class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # the max operations are delete all the chars of string1 and insert the char of string 2 which makes the maximum amount it requires which is O(n+M)
        # using recursive match??? like we need to match the source and the target string then may be it is easier to do that ?
        # trying all the cases insert or delete or replace then we go for the recursion !!!!
        # 1 express in terms of string matching (i,j) explore the all paths of matching 
        # return min of all the paths 
        # base case 
        # f(i,j) where i is for str1 and j is for str 2 f(n-1,m-1) find me the minimum number of operations to convert the str1 to str2 

        def traverse(str1,str2,i,j,dp):
            # base case
            # we think of this when its over 
            # if both are exhausted or if any one of the strings exhausted if str1 gets exhausted then the number of ooperations require empty string to make it string2 will be j+1
            # # recursion and memoisation 
            # if(i<0):
            #     return j+1 #insert operations 
            # if(j<0):
            #     return i+1 #delete operations

            # tabulation 
            for i in range(0,m+1):
                dp[i][0]=i
            for j in range(0,n+1):
                dp[0][j]=j

            # recursion with memoisation !
            # if(dp[i][j]!=-1):
            #     return dp[i][j]
            # # lets think if they mathced
            # if(str1[i]==str2[j]):
            #     # we dont need to do anytjing just return them 
            #     dp[i][j]= traverse(str1,str2,i-1,j-1,dp)
            #     return dp[i][j]
            #     # un matched condition where we can do either del or replace or insert 
            # # insert operation will go like 1+f(i,j-1) 
            # # delete oprtion will go like 1+f(i-1,j)
            # # replace condition ???? 1+f(i-1,j-1)
            # dp[i][j]= min(1+traverse(str1,str2,i,j-1,dp),1+traverse(str1,str2,i-1,j,dp),1+traverse(str1,str2,i-1,j-1,dp))
            # return dp[i][j]
            
            # tabulation 
            for i in range(1,m+1):
                for j in range(1,n+1):
                    if(str1[i-1]==str2[j-1]):
                        dp[i][j]= dp[i-1][j-1]
                    else:
                        dp[i][j]= 1+min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])
            return dp[m][n]
        
        # pass the params to the traverse 
        m=len(word1)
        n=len(word2)
        # lets get the fucking memoisation here !!!! which will be dp[m][n] memoisation 
        # dp=[[-1 for _ in range(n)] for _ in range(m)]
        # tabulation
        dp=[[-1 for _ in range(n+1)] for _ in range(m+1)]
        return traverse(word1,word2,m,n,dp)


# to remove the auxilary stack space we gor the tabulation to avoid the negative values we start with n+1 and m+1 for the tabulation. 
# so dp line changes by dp=[[-1 for _ in range(n+1)] for _ in range(m+1)]
# and the base case will change when they r equal to zero 
# two for loops when i ==0 or j==0 then dp [i][j] how they change 

