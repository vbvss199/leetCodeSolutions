import math
class Solution:
    def timecal(self,piles,hr):
        hours=0
        ans = max(piles)
        for i in range(len(piles)):
            hours += math.ceil(piles[i] / hr)
        return hours
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # for i in range(1,max(piles)+1):
        #     reqTime=self.timecal(piles,i)
        #     if reqTime <= h:
        #         return i

        # the above linear search with maxpiles needs to be replaced by the binary search 
        low=1
        high=max(piles)
        while(low<=high):
            mid=(low+high)//2
            reqTime=self.timecal(piles,mid)
            if reqTime<=h:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans