class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freqSet=set()
        left=0
        right=k-1
        windowSum=0
        maxSum=0
        windowAverage=0
        for i in range(left,right+1):
            while nums[i] in freqSet:
                freqSet.remove(nums[left])
                windowSum-=nums[left]
                left=left+1
            freqSet.add(nums[i])
            windowSum += nums[i]
        if right - left + 1 == k:
            maxSum = windowSum
        while(right<len(nums)-1):
            right=right+1
            # check if it exists in the freqSet and it is a valid window if exists else not
            while nums[right] in freqSet:
                freqSet.remove(nums[left])
                windowSum -= nums[left]
                left += 1 
            freqSet.add(nums[right])
            windowSum=windowSum+nums[right]
            # shrink the window if >k 
            if right - left + 1 > k:
                freqSet.remove(nums[left])
                windowSum -= nums[left]
                left += 1
            if right - left + 1 == k:
                maxSum = max(maxSum, windowSum)
        return maxSum
            

            # addd from right remove from left 