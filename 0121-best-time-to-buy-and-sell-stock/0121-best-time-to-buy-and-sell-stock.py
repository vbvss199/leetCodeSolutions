class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minEle=float("inf")
        profit=0
        for i in range(len(prices)):
            if(prices[i]<minEle):
                minEle=prices[i]
            profit=max(profit,prices[i]-minEle)
            
        return profit

    