class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freqMap={}
        for num in nums:
            freqMap[num]=freqMap.get(num, 0) + 1
            if freqMap[num]>1:
                return True
        return False