class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if(len(nums)<2):
            return 0
        maxGap=float("-inf")
        #sort the array 
        nums.sort()
        for i in range(1,len(nums)):
            maxGap=max(maxGap,nums[i]-nums[i-1])
        return maxGap