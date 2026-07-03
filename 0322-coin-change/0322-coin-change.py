class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [[-1 for _ in range(amount + 1)] for _ in range(len(coins))]

        def helper(i, target):
            if i == 0:
                if target % coins[0] == 0:
                    return target // coins[0]
                return float("inf")

            if dp[i][target] != -1:
                return dp[i][target]

            not_take = helper(i - 1, target)

            take = float("inf")
            if coins[i] <= target:
                take = 1 + helper(i, target - coins[i])

            dp[i][target] = min(take, not_take)
            return dp[i][target]

        ans = helper(len(coins) - 1, amount)
        return -1 if ans == float("inf") else ans