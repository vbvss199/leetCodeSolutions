class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # either from the start or the from the end we should pick consecutively
        # we can pick up the last 2 first two
        # pick the first three last one
        # last 3 first one 
        # the extreme naive solution would be pick 0 and 3 from end 
        # pick 3 from the start and one from end 
        # maintain leftsum and rightsum and calcualte the left sum using k elements first 
        # and take out one element from the left and expand right check using max condition and if update the max
        # maintain leftSum and rightSum and a global sum and everytime max(sum,rightSum+leftSum
        leftSum= sum(cardPoints[0:k])
        rightSum=0
        left=k
        maxSum=leftSum
        left=k-1
        right=len(cardPoints)-1
        # do k swaps 
        for _ in range(k):
            # start removing element from left and add from right 
            leftSum=leftSum-cardPoints[left]
            rightSum=rightSum+cardPoints[right]
            maxSum=max(maxSum,leftSum+rightSum)
            right=right-1
            left=left-1
        return maxSum