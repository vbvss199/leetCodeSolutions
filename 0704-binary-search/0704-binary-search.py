class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find in which half the target is present in first half or second half 
        start=0
        end=len(nums)
        while(start<end):
            mid=(start+end)//2
            if(target<nums[mid]):
                end=mid
            elif(target>nums[mid]):
                start=mid+1
            else:
                return mid
        return -1
    