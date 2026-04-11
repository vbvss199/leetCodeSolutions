class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # this problem is similar to the count sub array with sum equals k 
        # we take left and right , sum variable count=0
        # first write the condition like if sum equals inctrement the count 
        #  and increment the right 
        # and if right < len(nums) then add it to the sum 
        # now the condition like if sum exceeds and the left is still in the loop then remove the nums [left] and next increment the left ! 
        # while left <= right and if sum > k then move left 

        # now the current problem is array of binary numbers and goal is 2 
        # now we need to find the total number of sub array where the sum of the sub array is 2

        # lets fucking solve this 
        prefix_sum=0
        hashMap={0:1}
        count=0
        for num in nums:
            prefix_sum+=num
            if prefix_sum - goal in hashMap:
                count+=hashMap[prefix_sum-goal] 
            hashMap[prefix_sum] = hashMap.get(prefix_sum, 0) + 1
        return count