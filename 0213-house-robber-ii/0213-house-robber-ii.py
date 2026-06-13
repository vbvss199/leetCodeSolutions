class Solution:
    def rob(self, nums: List[int]) -> int:
        # similar to house robber 1 but this is a circle now , houses arranged in a circle 
        temp1=[]
        temp2=[]
        n=len(nums)
        if(n==1):
            return nums[0]
        for i in range(n):
            if(i!=0):
                temp1.append(nums[i])
            if(i!=n-1):
                temp2.append(nums[i])
        # uncomment below line if we r following recursion
        condition1=self.maxSubSequence(temp1,0,{})
        condition2=self.maxSubSequence(temp2,0,{})
        answer=max(condition1,condition2)
        return answer

    def maxSubSequence(self,nums,i,dp):
        # we need to write a logic such that it should not treat first and last as same , circle condition 
        # initial condition
        if(i>=len(nums)):
            return 0
        # dp condition
        if i in dp:
            return dp[i]
        # pick condition
        pick=nums[i]+self.maxSubSequence(nums,i+2,dp)
        # not pick condition 
        not_pick=0+self.maxSubSequence(nums,i+1,dp)
        dp[i]=max(pick,not_pick)
        return dp[i]




# removing first and last is impossible , what if if we leave first element and apply the logic above or the last element and apply th elogic 
# if we leave first element and start the maxSubSequence from 2nd and leave the last elemnt and out of these the max is the answer 