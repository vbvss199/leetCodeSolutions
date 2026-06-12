class Solution:
    def rob(self, nums: List[int]) -> int:
        # the answer may not lie in the single house skipping it may lie in the two or more sometimes 
        # this can be solved using the DP but think it , and more over we need to return the maximum here !!!!!
        # one point is clear we need to go from starting to end 
        #  in 2 1.4. 9 we pick 2 and 9 to get the max 
        # sub array must be contiguous and 
        #  sub sequence is something we can skip element but order must be preserved
        # try out all the sub sequences and try out the one which has maximum sum 
        # try recursion and see if there are overlapping sub problems and then we can go to the other 
        # theres a technique called pick and non pick but picking and non picking make sure they are not adjacent ! and thats it then out of them pick the one which is best one !!!!!
        # if we pick we take sum=a[index] and not pick will be 0+
        # and one more thing if we check if i==0 then print it , we start from f(nums,n) and if we do i==n then it is f(nums,0)
        # to store the occurances !!!
        dp=[-1]*len(nums)
        return self.maxSubSequence(nums,0,dp)
    # def maxSubSequence(self,nums: List[int],i:int) -> int:
    #     if(i>=len(nums)):
    #         #if we reach the end theers nothung 
    #         return 0
    #     #and track the sum using the pick and no pick variable 
    #     pick=nums[i]+self.maxSubSequence(nums,i+2)
    #     not_pick=0+self.maxSubSequence(nums,i+1)
    #     sum=max(pick,not_pick)
    #     return sum

    
    # so here comes the overlapping sub problem if we r calcualting anything repeatdly so use DP 
    # but how come ? using the dict as in the evry moment we r storing the sum which is max instead store in the dp[i]
    def maxSubSequence(self,nums: List[int],i:int,dp) -> int:
        if(i>=len(nums)):
            #if we reach the end theers nothung 
            return 0
        # there will be a some logic like if dp[i]!=-1 then return dp[i]
        if(dp[i]!=-1):
            return dp[i]
        #and track the sum using the pick and no pick variable 
        pick=nums[i]+self.maxSubSequence(nums,i+2,dp)
        not_pick=0+self.maxSubSequence(nums,i+1,dp)
        dp[i]=max(pick,not_pick)
        return dp[i]