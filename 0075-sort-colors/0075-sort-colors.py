class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low=mid=0
        high=len(nums)-1
        # divide the array in such a way based on the mid element swap it to the ledt if 0 and to the right if it is 2 and 1 just move the mid pointer 
        while(mid<=high):
            # case 1 
            if(nums[mid]==0):
                nums[mid],nums[low]=nums[low],nums[mid]
                low=low+1
                mid=mid+1
            # case 2 , just incremenet the mid pointer 
            elif(nums[mid]==1):
                mid=mid+1
            # case 3 swap with the right most element and decrement the right or high ,dont trust the right pointer so dont increment the mid as it is 0 or 1 or 2 so keep the mid as it is 
            elif(nums[mid]==2):
                nums[mid],nums[high]=nums[high],nums[mid]
                high=high-1
        return nums


