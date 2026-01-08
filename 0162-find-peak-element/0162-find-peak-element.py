class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # question solved while learning DSA with bhatt
        # low,high=0,len(nums)-1
        # n=len(nums)
        # if(n==1):
        #     return 0
        # while(low<=high):
        #     mid=(low+high)//2
        #     if(mid==0 and nums[mid]>nums[mid+1]) or (mid==n-1 and nums[mid]>nums[mid-1]) or (nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]):
        #         return mid
        #     elif(nums[mid]<nums[mid+1]):
        #         low=mid+1
        #     else:
        #         high=mid-1
        # return -1        

        # strivers solution !
        # similar kind 
        low,high=0,len(nums)-1
        if(len(nums)==1):
            return 0
        while(low<=high):
            mid=(low+high)//2
            if( (mid==0 and nums[mid]>nums[mid+1]) or (mid==len(nums)-1 and nums[mid]>nums[mid-1]) or (nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1])):
                return mid
            elif(nums[mid]<nums[mid+1]):
                low=mid+1
            else:
                high=mid-1
        return -1 