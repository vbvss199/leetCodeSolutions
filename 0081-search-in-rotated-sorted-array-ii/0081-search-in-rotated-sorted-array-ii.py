class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low=0
        high=len(nums)-1
        while(low<=high):
            mid=(low+high)//2
            # in the first go if we got just return true
            if(nums[mid]==target):
                return True
            if(nums[low]==nums[mid] and nums[mid]==nums[high]):
                low=low+1
                high=high-1
                continue
            # left half sorted    
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
        return False