class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # get thte unique ways to get the target by using + or -
        # how many ways can we assign the given signs 
        # for each number there r two  possibilities either we take plus or negative then count by adding plus +negative if it hits the target  
        def traverse(index,sum,dp):
            # if we used all the numbers that means we reached end 
            # this is our base case 
            if(index==len(nums)):
                if(target==sum):
                    return 1
                else:
                    return 0
            
            # check the dp if exists 
            if dp[index][sum] is not None:
                return dp[index][sum]
            
            # else continue with the recursion 
            # positive or negative
            positive=traverse(index+1,sum+nums[index],dp)
            negative=traverse(index+1,sum-nums[index],dp)
            dp[index][sum] = positive+negative
            return dp[index][sum]

        # call this function by passing the require params and see 
        # lets go with the dp now 
        total = sum(nums)

        dp = [[None for _ in range(2 * total + 1)] for _ in range(len(nums))]
        return traverse(0,0,dp)
        