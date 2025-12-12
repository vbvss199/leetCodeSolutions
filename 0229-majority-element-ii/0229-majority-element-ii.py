class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freqMap={}
        ans=[]
        for i in range(len(nums)):
            freqMap[nums[i]]=freqMap.get(nums[i], 0) + 1
        for key, val in freqMap.items():
            if val > len(nums)//3:
                ans.append(key)
        return ans

        