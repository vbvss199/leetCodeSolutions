class Solution:
    def mySqrt(self, x: int) -> int:
        ans=1
        if(x==0):
            return 0
        else:
            for i in range(1,x):
                if i*i<=x:
                    ans=i
                else:
                    break
        return ans