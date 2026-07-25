class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # we can skip the elements 
        # instead of the traditional recursion improvised tabulation is used directly here 
        def lcs(m,n,dp,s,s1):
            # we got m , n and dp
            # 1 the base case keep as it is 
            for i in range(0,m+1):
                dp[i][0]=0
            for j in range(0,n+1):
                dp[0][j]=0
            
            # now the iterative condition 
            # as tabulation is bottom up and we already done with the base case so the below starts from 1 
            for i in range(1,m+1):
                for j in range(1,n+1):
                    # make sure to remoeve 1 from the s and s1 i and j
                    if(s[i-1] == s1[j-1]):
                        dp[i][j]=1+dp[i-1][j-1]
                    else:
                        dp[i][j]=max(dp[i-1][j],dp[i][j-1])
            return dp[m][n]
            

        # pass the two params which are m ,n here in this they are equal 
        # the idea is to reverse the string and pass it to the lcs method and find the lcs 
        s1=s[::-1]
        # for the sake just trteat it as separate and calcualte the 
        m=len(s)
        n=len(s1)
        dp=[[-1 for _ in range(n+1)] for _ in range(m+1)] #where m are rows and n are columns !!!

        # call the method with m,n, and dp
        return lcs(m,n,dp,s,s1)