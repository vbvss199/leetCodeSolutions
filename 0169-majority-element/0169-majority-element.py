class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freqMap={}
        n=len(nums)
        for i in range(len(nums)):
            freqMap[nums[i]]=freqMap.get(nums[i],0)+1
        max_key = max(freqMap, key=freqMap.get)
        return max_key