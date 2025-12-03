class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a hashmap which stores the element and its index as key-value pairs
        hashmap={}
        for i in range(len(nums)):
            if(target-nums[i]) in hashmap:
                x = [i,hashmap[target-nums[i]]]
            else:
                hashmap[nums[i]]=i
        return x