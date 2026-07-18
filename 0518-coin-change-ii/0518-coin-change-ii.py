class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[-1 for _ in range(amount + 1)] for _ in range(len(coins))]

        def helper(i, target):
            # base case will be always reaching end or start 
            if i == 0:
                # if we reahed index 0 then the given coin if it is dividing exactly by the target then we return the number of coins which is the quotient 
                if target % coins[0] == 0:
                    return 1
                return 0

            if dp[i][target] != -1:
                return dp[i][target]

            not_take = 0+helper(i - 1, target)

            # if we r looking for minimum so assign to max and for minimum we go with max viceversa !!!
            take = 0
            if coins[i] <= target:
                take = helper(i, target - coins[i])

            dp[i][target] = take + not_take
            return dp[i][target]

        ans = helper(len(coins) - 1, amount)
        return ans
        