class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # greedy approach 
        # finding the possibilities that we can go from the given nums[i] based on the length see if we can reach the end with that 
        # try all possible combinations 
        # theres a pattern if a array has a positive integers all we can reach the end 
        # if it has a zero then its difficult to reach the end 
        # approach -> if we r the at the element get the index and add with the max jumps and update the maxIndex variable /if the maxIndex reaches the end(last index) which is len(nums)-1 then return True else return False ! 
        # maxIndex=0
        # for i in range(len(nums)):
        #     if(maxIndex<i):
        #         return False
        #         # the below line indicates at the position i we can jump max of array[i] to the right , so at any index the farthest index we can reach is i+array[i]
        #     maxIndex=max(maxIndex,i+nums[i])
        # return True

        # approach 2
        destination=len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            # at any momenet the 
            if nums[i]+i >= destination:
                # then the current index will be our destination 
                destination=i
        return destination==0