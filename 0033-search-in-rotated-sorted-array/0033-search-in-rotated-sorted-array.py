class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        while(low<=high):
            mid=(low+high)//2
            if(nums[mid]==target):
                return mid
            # case either left half is sorted 
            elif(nums[low]<=nums[mid]):
                if((nums[low]<=target) and (target<=nums[mid])):
                    high=mid-1
                else:
                    low=mid+1
            # case right side is sorted 
            else:
                if((nums[mid]<=target) and (target<=nums[high])):
                    low=mid+1
                else:
                    high=mid-1
        return -1
    # the binary search approach works only in the sorted array ,