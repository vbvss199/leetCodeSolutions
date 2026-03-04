class Solution:
    def f(self,n:int)-> int:
        if(n<=1):
            return n
        if self.dp[n]!=-1:
            return self.dp[n]
        self.dp[n]=self.f(n-1) + self.f(n-2)
        return self.dp[n]
    def fib(self, n: int) -> int:
        # if(n==0):
        #     return 0
        # elif(n==1):
        #     return 1
        # else:
        #     return self.fib(n-1)+self.fib(n-2)
        
        # lets solve using DP 
        self.dp=[-1]*(n+1)
        return self.f(n)