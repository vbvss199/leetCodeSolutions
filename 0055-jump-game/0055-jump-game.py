class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # greedy approach 
        # finding the possibilities that we can go from the given nums[i] based on the length see if we can reach the end with that 
        # try all possible combinations 
        # theres a pattern if a array has a positive integers all we can reach the end 
        # if it has a zero then its difficult to reach the end 
        # approach -> if we r the at the element get the index and add with the max jumps and update the maxIndex variable /if the maxIndex reaches the end(last index) which is len(nums)-1 then return True else return False ! 
        maxIndex=0
        for i in range(len(nums)):
            if(maxIndex<i):
                return False
            maxIndex=max(maxIndex,i+nums[i])
        return True