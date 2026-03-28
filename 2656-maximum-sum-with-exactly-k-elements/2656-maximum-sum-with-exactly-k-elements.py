class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        max_sum = max(nums)
        return k*(max_sum)+(k*(k-1)//2)