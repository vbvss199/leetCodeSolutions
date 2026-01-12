import math
class Solution:
    # run a loop and return if it matches the threshold
    def calThreshold(self,nums,number,threshold):
        loc_threshold=0
        for i in range(len(nums)):
            loc_threshold=loc_threshold+math.ceil(nums[i]/number)
        if(loc_threshold<=threshold):
            return True
        else:
            return False

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # naive approach
        # for i in range(1,max(nums)+1):
        #     if(self.calThreshold(nums,i,threshold)==True):
        #         return i
        # lets go and hit the binary search approach
        low=1
        high=max(nums)
        answer=1
        while(low<=high):
            mid=(low+high)//2
            if(self.calThreshold(nums,mid,threshold)==True):
                answer=mid
                high=mid-1
            else:
                low=mid+1
        return answer
