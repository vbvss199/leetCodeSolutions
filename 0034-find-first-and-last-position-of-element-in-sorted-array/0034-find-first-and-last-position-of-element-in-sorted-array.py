class Solution:
    answerFirst=-1
    answerLast=-1
    def firstElement(self,nums,target):
        # finding the smallest index possible for the target 
        # as the array is already sprted we will eliminate the right side completly
        low=0
        high=len(nums)-1
        while(low<=high):
            mid=(low+high)//2
            if nums[mid] == target:
                self.answerFirst = mid
                high = mid - 1      # keep going left or eliminate right 
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return self.answerFirst
    def lastElement(self,nums,target):
        low=0
        high=len(nums)-1
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]==target:
                self.answerLast=mid
                low=mid+1
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return self.answerLast
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.firstElement(nums, target), self.lastElement(nums, target)]
