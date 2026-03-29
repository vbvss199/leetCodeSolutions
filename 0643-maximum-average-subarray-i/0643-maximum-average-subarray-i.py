class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left=0
        right=k-1
        windowSum=0
        maxAverage=0
        windowAverage=0
        for i in range(left,right+1):
            windowSum+=nums[i]
        maxAverage=windowSum/k
        windowAverage=windowSum/k
        while(right<len(nums)-1):
            windowSum=windowSum-nums[left]
            left=left+1
            right=right+1
            windowSum=windowSum+nums[right]
            windowAverage=windowSum/k
            maxAverage=max(windowAverage,maxAverage)
        return maxAverage
            