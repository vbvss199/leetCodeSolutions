class Solution:
    def minInsertions(self, s: str) -> int:
        # the lcs and max len of a palindrominc string problem together 
        # so what we do is come with the idea to find the longest palindrome which is ontact
        # for supose abcaa th4 elongest is aaa so the left out part is bc make sure to arrange another bc such that we make it as a palindromic string 
        # similar way the minimum insertions formule , revise the strivers video 
        # is len(string)-longest palindromic string in the given string 

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
            return len(s)-dp[m][n]
        
        s1=s[::-1]
        m=len(s)
        n=len(s1)

        dp=[[-1 for _ in range(n+1)] for _ in range(m+1)]
        return lcs(m,n,dp,s,s1)