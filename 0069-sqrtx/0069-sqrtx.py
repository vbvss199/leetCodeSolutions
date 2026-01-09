class Solution:
    def mySqrt(self, x: int) -> int:
        # ans=1
        # if(x==0):
        #     return 0
        # else:
        #     for i in range(1,x):
        #         if i*i<=x:
        #             ans=i
        #         else:
        #             break
        # return ans
        
        # lets try the binary search approach
        ans = 0
        low=1
        high=x
        while(low<=high):
            mid=(low+high)//2
            if (mid*mid == x):
                return mid
            elif(mid*mid < x):
                ans = mid
                low=mid+1
            else:
                high=mid-1
        return ans