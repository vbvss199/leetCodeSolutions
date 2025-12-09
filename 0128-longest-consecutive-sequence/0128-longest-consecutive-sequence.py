class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        freqMap={}
        currentCount=0
        maxCount=0
        for i in range(len(nums)):
             freqMap[nums[i]] = freqMap.get(nums[i], 0) + 1
        # this can be reduced in order to remove the loop time complexity above and can be converted to set which reduces the TC
        for x in freqMap:
            if x - 1 not in freqMap:
                currentCount=1
                currentElement=x
                while currentElement + 1 in freqMap:
                    currentCount=currentCount+1
                    currentElement=currentElement+1
                maxCount=max(currentCount,maxCount)
        return maxCount